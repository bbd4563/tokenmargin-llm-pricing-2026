#!/usr/bin/env python3
"""
Zero-dependency 2026 LLM API & Multi-Turn Agent Loop Cost Calculator.
Live dataset & interactive SaaS margin stress-tester: https://tokenmargin.dev
"""
import argparse
import json
import os
import urllib.request

LOCAL_JSON = os.path.join(os.path.dirname(__file__), "llm-pricing-2026.json")


def load_models():
    if os.path.exists(LOCAL_JSON):
        with open(LOCAL_JSON, "r", encoding="utf-8") as f:
            return json.load(f)["models"]
    with urllib.request.urlopen("https://tokenmargin.dev/api/v1/models", timeout=10) as r:
        return json.loads(r.read().decode("utf-8"))["models"]


def main():
    parser = argparse.ArgumentParser(description="2026 LLM API & Multi-Turn Agent Cost Calculator (TokenMargin.dev)")
    parser.add_argument("--model", default="anthropic/claude-sonnet-5.5", help="Model ID (e.g. anthropic/claude-sonnet-5.5, liquid/d1.2-ultra, qwen/qwen4-max)")
    parser.add_argument("--dau", type=int, default=1000, help="Daily Active Users (default: 1000)")
    parser.add_argument("--tasks-per-day", type=float, default=5.0, help="Tasks per user per day (default: 5)")
    parser.add_argument("--turns", type=int, default=15, help="Agent turns per task (default: 15)")
    parser.add_argument("--prefix-tokens", type=int, default=10000, help="Static system + repo/MCP prefix tokens (default: 10000)")
    parser.add_argument("--turn-Context-growth", type=int, default=1500, help="New tool/context tokens added per turn (default: 1500)")
    parser.add_argument("--output-per-turn", type=int, default=450, help="Output tokens per turn (default: 450)")
    parser.add_argument("--cache-hit", type=float, default=0.80, help="Prefix cache hit ratio 0.0-0.95 (default: 0.80)")
    args = parser.parse_args()

    models = load_models()
    by_id = {m["id"].lower(): m for m in models}
    m = by_id.get(args.model.lower())
    if not m:
        matches = [x for x in models if args.model.lower() in x["id"].lower() or args.model.lower() in x["name"].lower()]
        if not matches:
            print(f"Model '{args.model}' not found. Run without args or browse all 470+ models at https://tokenmargin.dev")
            return
        m = matches[0]

    # Cumulative input tokens across N turns: N * prefix + growth * N * (N - 1) / 2
    cum_input = args.turns * args.prefix_tokens + args.turn_Context_growth * (args.turns * (args.turns - 1) / 2.0)
    cum_output = args.turns * args.output_per_turn

    cached_in = cum_input * max(0.0, min(0.95, args.cache_hit))
    uncached_in = cum_input - cached_in

    in_rate = float(m["inputPricePer1M"])
    out_rate = float(m["outputPricePer1M"])
    cache_rate = float(m.get("cacheReadPricePer1M", in_rate * 0.5))

    cost_uncached_task = (cum_input / 1e6) * in_rate + (cum_output / 1e6) * out_rate
    cost_cached_task = (uncached_in / 1e6) * in_rate + (cached_in / 1e6) * cache_rate + (cum_output / 1e6) * out_rate
    monthly_tasks = args.dau * args.tasks_per_day * 30.0

    print(f"=== {m['name']} ({m['id']}) ===")
    print(f"Rates per 1M    : ${in_rate} in | ${out_rate} out | ${cache_rate} cached read")
    print(f"Tokens / Task   : {int(cum_input):,} cumulative input + {int(cum_output):,} output ({args.turns} turns)")
    print(f"Cost / Task     : ${cost_cached_task:.4f} (with {int(args.cache_hit*100)}% cache) vs ${cost_uncached_task:.4f} uncached")
    print(f"Monthly ({args.dau:,} DAU): ${cost_cached_task * monthly_tasks:,.2f}/mo (saves ${(cost_uncached_task - cost_cached_task) * monthly_tasks:,.2f}/mo via prefix cache)")
    print(f"Interactive UI  : https://tokenmargin.dev/?tab=margin&model={m['id']}&ref=github_cli")


if __name__ == "__main__":
    main()
