# 2026 LLM API Pricing Table & Python Cost Calculator (470+ Models)

[![Live FinOps Terminal](https://img.shields.io/badge/Live_Calculator-TokenMargin.dev-10b981?style=for-the-badge)](https://tokenmargin.dev/?ref=github)
[![Models Synced](https://img.shields.io/badge/Models_Indexed-470+-06b6d4?style=for-the-badge)](https://tokenmargin.dev/directory.html?ref=github)
[![Zero Upload CSV Audit](https://img.shields.io/badge/CSV_Bill_Auditor-100%25_Browser_Local-f59e0b?style=for-the-badge)](https://tokenmargin.dev/guides/openrouter-openai-anthropic-csv-bill-analyzer.html?ref=github)

Open-source, auto-updated **2026 LLM API Pricing Dataset (`llm-pricing-2026.json`)**, **Zero-Dependency Python Token & Multi-Turn Agent Loop Cost Calculator (`llm_cost_calculator.py`)**, and **SaaS Gross Margin Stress-Test Benchmarks** synced every 6 hours from OpenRouter, Models.dev, and LiteLLM via **[TokenMargin.dev](https://tokenmargin.dev/?ref=github)**.

---

## Quick Start: Python CLI Cost Calculator (Zero Dependencies)

```bash
python llm_cost_calculator.py --model anthropic/claude-sonnet-5.5 --dau 10000 --turns 20 --cache-hit 0.85
```

Or run interactive scenarios in your browser (including **0-byte local OpenAI / Anthropic / OpenRouter Usage CSV Bill Auditing**, **Claude Max $100/$200 vs API Key Break-Even**, and **40-line zero-dependency TypeScript/Python router generation**) at **[https://tokenmargin.dev](https://tokenmargin.dev/?ref=github)**.

---

## Featured 2026 Production AI FinOps Benchmarks & Calculators

- **[Freebuff vs DeepSeek Harness vs OpenCode vs Factory: 2026 Parallel-Tool-Call CLI Coding Speed & API Cost Benchmark](https://tokenmargin.dev/guides/freebuff-vs-deepseek-harness-vs-opencode-vs-factory-cost-benchmark.html?ref=github)** — Production 2026 coding harness audit comparing Freebuff (90.6B OpenRouter tokens/day, ad-supported free coding models + parallel-tool-call D...
- **[vLLM vs SGLang vs Ollama vs llama.cpp: 2026 GPU Throughput, KV-Cache & Cost per 1M Tokens Calculator](https://tokenmargin.dev/guides/vllm-vs-sglang-vs-ollama-vs-llamacpp-gpu-throughput-cost-calculator.html?ref=github)** — Why serving engine choice changes your self-hosted H100 / B300 GPU cost-per-1M-tokens by 3x–6x: compare SGLang (RadixAttention prefix KV-cac...
- **[Groq LPU vs Cerebras Wafer-Scale: 2026 Tokens/Sec Speed, <150ms TTFT & API Pricing Benchmark](https://tokenmargin.dev/guides/groq-lpu-vs-cerebras-wafer-scale-speed-ttft-pricing-benchmark.html?ref=github)** — Head-to-head 2026 benchmark comparing Groq LPU and Cerebras Wafer-Scale Engine (WSE-3) across Time-to-First-Token (TTFT), output streaming v...
- **[AWS Bedrock vs Google Vertex AI vs Azure AI Foundry: 2026 Enterprise LLM Pricing Calculator](https://tokenmargin.dev/guides/aws-bedrock-vs-google-vertex-ai-vs-azure-foundry-pricing-calculator.html?ref=github)** — Compare 2026 on-demand, Global Cross-Region Inference, Provisioned Throughput (PTU), Batch (-50%), and Prompt Caching token prices across AW...
- **[LiteLLM vs Bifrost vs Portkey vs AgentGateway: 2026 AI Gateway Latency, Overhead & Cost Benchmark](https://tokenmargin.dev/guides/litellm-vs-bifrost-vs-portkey-vs-agentgateway-benchmark-2026.html?ref=github)** — Production 2026 architecture benchmark comparing LiteLLM (Python proxy), Maxim Bifrost (ultra-low-latency Go gateway), Portkey AI, AgentGate...
- **[RunPod vs Vast.ai vs Modal vs Lambda Labs: 2026 H100, H200 & B300 GPU Pricing & Break-Even Calculator](https://tokenmargin.dev/guides/runpod-vs-vast-ai-vs-modal-vs-lambda-labs-gpu-pricing-2026.html?ref=github)** — Side-by-side 2026 GPU $/hr, cold-start latency, Serverless Batch (-30%), and effective cost-per-1M-tokens benchmark across RunPod, Vast.ai, ...
- **[OpenRouter vs OpenCode (Zen & Go) vs Kilo Code: 2026 CLI Coding API Pricing & Token Burn Calculator](https://tokenmargin.dev/guides/openrouter-vs-opencode-zen-go-kilo-code-pricing-calculator.html?ref=github)** — Head-to-head 2026 unit-economics audit comparing OpenRouter BYOK (0% token markup across 469+ models + Hugging Face routing), OpenCode Zen (...
- **[Claude Max ($100 / $200) vs API Key (BYOK) & Cursor Max Mode Cost Break-Even Calculator (2026)](https://tokenmargin.dev/guides/claude-max-vs-api-key-cursor-max-mode-cost-break-even-calculator.html?ref=github)** — At how many daily Claude Code or Cursor Max Mode sessions does a $100/mo (5x) or $200/mo (20x) Claude Max plan beat paying Anthropic or Open...
- **[Liquid AI d1.2 & d1.2-ultra API Pricing ($0.02 / $0.042 Input, $0 Output): Decision Models vs Autoregressive LLMs Calculator (2026)](https://tokenmargin.dev/guides/liquid-ai-d1-2-ultra-zero-output-token-decision-model-pricing-calculator.html?ref=github)** — Complete Nov 2026 unit-economics audit of Liquid AI d1.2 ($0.02/1M input, $0.00 output) and d1.2-ultra ($0.042/1M input, $0.00 output)—ranke...
- **[Hermes Agent vs Kilo Code vs Claude Code vs OpenClaw: OpenRouter BYOK Token Cost & 80/20 Router Calculator (2026)](https://tokenmargin.dev/guides/hermes-agent-kilo-code-claude-code-openclaw-openrouter-cost-calculator.html?ref=github)** — Why Hermes Agent (1.71T tokens/day), Kilo Code (1.21T/day), Claude Code (1.17T/day), OpenClaw, and OpenHands lead OpenRouter daily traffic—a...
- **[Hugging Face × OpenRouter Unified Inference Routing vs Pinned GPU Hosts: Prefix KV-Cache, TTFT & Broadcast Distillation Calculator (2026)](https://tokenmargin.dev/guides/huggingface-openrouter-inference-routing-pricing-kv-cache-guide.html?ref=github)** — Complete Nov 2026 architecture and unit-economics audit of Hugging Face open-model inference running on OpenRouter (single HF_TOKEN auto-fai...
- **[OpenRouter, OpenAI & Anthropic Usage CSV Bill Analyzer: 100% Client-Side LLM FinOps Audit Calculator (2026)](https://tokenmargin.dev/guides/openrouter-openai-anthropic-csv-bill-analyzer.html?ref=github)** — Drop your 30-day OpenRouter, Anthropic Console, OpenAI API, or Cursor/Cline usage CSV or JSONL file to run a 100% browser-local FinOps audit...

---

## Complete 2026 LLM API Pricing Matrix (120 Curated Models — USD per 1M Tokens)

*Last synced: `2026-11-17T01:52:37.893Z`*

| Model & Live Calculator | API Model ID | Provider | Input / 1M | Output / 1M | Cache Read / 1M | Context |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **[Llama 3.2 3B Instruct (Edge/Router)](https://tokenmargin.dev/models/llama-3-2-3b-instruct-pricing-calculator.html?ref=github)** | `meta-llama/llama-3.2-3b-instruct` | DeepInfra | **$0.015** | **$0.025** | $0.008 | 131K |
| **[Liquid AI d1.2](https://tokenmargin.dev/models/d1-2-pricing-calculator.html?ref=github)** | `liquid/d1.2` | Liquid AI | **$0.02** | **$0** | $0.01 | 131K |
| **[Llama 3.1 8B Instruct](https://tokenmargin.dev/models/llama-3-1-8b-instruct-pricing-calculator.html?ref=github)** | `meta-llama/llama-3.1-8b-instruct` | Groq | **$0.03** | **$0.05** | $0.015 | 131K |
| **[Amazon Nova Micro v1](https://tokenmargin.dev/models/nova-micro-v1-pricing-calculator.html?ref=github)** | `amazon/nova-micro-v1` | OpenRouter | **$0.035** | **$0.14** | $0.0088 | 128K |
| **[DeepSeek V4.1 Flash 1017](https://tokenmargin.dev/models/deepseek-v4-1-flash-1017-pricing-calculator.html?ref=github)** | `deepseek/deepseek-v4.1-flash-1017` | DeepSeek | **$0.036** | **$0.5** | $0.01 | 1M |
| **[Cohere Command R7B (Fast RAG)](https://tokenmargin.dev/models/command-r7b-12-2024-pricing-calculator.html?ref=github)** | `cohere/command-r7b-12-2024` | OpenRouter | **$0.0375** | **$0.15** | $0.019 | 128K |
| **[Qwen 2.5 7B Instruct](https://tokenmargin.dev/models/qwen-2-5-7b-instruct-pricing-calculator.html?ref=github)** | `qwen/qwen-2.5-7b-instruct` | DeepInfra | **$0.04** | **$0.1** | $0.02 | 131K |
| **[DeepSeek R1 Distill Llama 8B](https://tokenmargin.dev/models/deepseek-r1-distill-llama-8b-pricing-calculator.html?ref=github)** | `deepseek/deepseek-r1-distill-llama-8b` | DeepInfra | **$0.04** | **$0.04** | $0.02 | 131K |
| **[Liquid AI d1.2-ultra](https://tokenmargin.dev/models/d1-2-ultra-pricing-calculator.html?ref=github)** | `liquid/d1.2-ultra` | Liquid AI | **$0.042** | **$0** | $0.021 | 131K |
| **[Hy4 flash](https://tokenmargin.dev/models/hy4-flash-pricing-calculator.html?ref=github)** | `tencent/hy4-flash` | Tencent Hunyuan | **$0.0437** | **$0.1756** | $0.0019 | 1M |
| **[Ling 3.1 Flash](https://tokenmargin.dev/models/ling-3-1-flash-pricing-calculator.html?ref=github)** | `inclusionai/ling-3.1-flash` | inclusionAI | **$0.045** | **$0.135** | $0.009 | 1M |
| **[Llama 3.2 11B Vision Instruct](https://tokenmargin.dev/models/llama-3-2-11b-vision-instruct-pricing-calculator.html?ref=github)** | `meta-llama/llama-3.2-11b-vision-instruct` | DeepInfra | **$0.049** | **$0.049** | $0.025 | 131K |
| **[Qwen Turbo (1M Context)](https://tokenmargin.dev/models/qwen-turbo-pricing-calculator.html?ref=github)** | `qwen/qwen-turbo` | OpenRouter | **$0.05** | **$0.2** | $0.025 | 1M |
| **[Mistral Small 3.1 24B Instruct](https://tokenmargin.dev/models/mistral-small-3-1-24b-instruct-pricing-calculator.html?ref=github)** | `mistralai/mistral-small-3.1-24b-instruct` | DeepInfra | **$0.05** | **$0.1** | $0.025 | 128K |
| **[Amazon Nova Lite v1](https://tokenmargin.dev/models/nova-lite-v1-pricing-calculator.html?ref=github)** | `amazon/nova-lite-v1` | OpenRouter | **$0.06** | **$0.24** | $0.015 | 300K |
| **[Microsoft Phi-4 (14B Dense)](https://tokenmargin.dev/models/phi-4-pricing-calculator.html?ref=github)** | `microsoft/phi-4` | DeepInfra | **$0.06** | **$0.14** | $0.03 | 16K |
| **[Qwen 2.5 Coder 32B Instruct](https://tokenmargin.dev/models/qwen-2-5-coder-32b-instruct-pricing-calculator.html?ref=github)** | `qwen/qwen-2.5-coder-32b-instruct` | DeepInfra | **$0.07** | **$0.16** | $0.035 | 33K |
| **[Gemini 2.0 Flash-Lite](https://tokenmargin.dev/models/gemini-2-0-flash-lite-001-pricing-calculator.html?ref=github)** | `google/gemini-2.0-flash-lite-001` | Google | **$0.075** | **$0.3** | $0.019 | 1M |
| **[Gemini 1.5 Flash](https://tokenmargin.dev/models/gemini-1-5-flash-pricing-calculator.html?ref=github)** | `google/gemini-1.5-flash` | Google | **$0.075** | **$0.3** | $0.0187 | 1M |
| **[Llama 4 Scout (10M Context MoE)](https://tokenmargin.dev/models/llama-4-scout-pricing-calculator.html?ref=github)** | `meta-llama/llama-4-scout` | Groq | **$0.08** | **$0.3** | $0.04 | 1M |
| **[LFM3-1.7B](https://tokenmargin.dev/models/lfm-3-1-7b-pricing-calculator.html?ref=github)** | `liquid/lfm-3-1.7b` | Liquid AI | **$0.08** | **$0.2** | $0.02 | 262K |
| **[Gemini 2.0 Flash](https://tokenmargin.dev/models/gemini-2-0-flash-001-pricing-calculator.html?ref=github)** | `google/gemini-2.0-flash-001` | Google | **$0.1** | **$0.4** | $0.025 | 1M |
| **[Ministral 8B](https://tokenmargin.dev/models/ministral-8b-pricing-calculator.html?ref=github)** | `mistralai/ministral-8b` | OpenRouter | **$0.1** | **$0.1** | $0.05 | 131K |
| **[Google Gemma 3 27B Instruct](https://tokenmargin.dev/models/gemma-3-27b-it-pricing-calculator.html?ref=github)** | `google/gemma-3-27b-it` | DeepInfra | **$0.1** | **$0.2** | $0.05 | 131K |
| **[GPT-4.1 Nano (Ultra-Fast Router)](https://tokenmargin.dev/models/gpt-4-1-nano-pricing-calculator.html?ref=github)** | `openai/gpt-4.1-nano` | OpenAI | **$0.1** | **$0.4** | $0.03 | 1M |
| **[Muse Ember](https://tokenmargin.dev/models/muse-ember-pricing-calculator.html?ref=github)** | `meta/muse-ember` | Meta AI | **$0.1** | **$0.5** | $0.004 | 1M |
| **[Claude Haiku 5.5](https://tokenmargin.dev/models/claude-haiku-5-5-pricing-calculator.html?ref=github)** | `anthropic/claude-haiku-5.5` | Anthropic | **$0.1** | **$0.5** | $0.01 | 1M |
| **[GPT-6 Luna Pro](https://tokenmargin.dev/models/gpt-6-luna-pro-pricing-calculator.html?ref=github)** | `openai/gpt-6-luna-pro` | OpenAI | **$0.1** | **$0.5** | $0.01 | 1M |
| **[GPT-6 Luna](https://tokenmargin.dev/models/gpt-6-luna-pricing-calculator.html?ref=github)** | `openai/gpt-6-luna` | OpenAI | **$0.1** | **$0.5** | $0.01 | 1M |
| **[DeepSeek V4 Pro 0813](https://tokenmargin.dev/models/deepseek-v4-pro-0813-pricing-calculator.html?ref=github)** | `deepseek/deepseek-v4-pro-0813` | DeepSeek | **$0.111** | **$4.44** | $0.097 | 1M |
| **[DeepSeek R1 Distill Qwen 32B](https://tokenmargin.dev/models/deepseek-r1-distill-qwen-32b-pricing-calculator.html?ref=github)** | `deepseek/deepseek-r1-distill-qwen-32b` | DeepInfra | **$0.12** | **$0.18** | $0.06 | 131K |
| **[Llama 3.3 70B Instruct](https://tokenmargin.dev/models/llama-3-3-70b-instruct-pricing-calculator.html?ref=github)** | `meta-llama/llama-3.3-70b-instruct` | DeepInfra | **$0.12** | **$0.3** | $0.06 | 131K |
| **[Qwen QwQ-32B (Reasoning)](https://tokenmargin.dev/models/qwq-32b-pricing-calculator.html?ref=github)** | `qwen/qwq-32b` | DeepInfra | **$0.12** | **$0.18** | $0.06 | 131K |
| **[Qwen 2.5 72B Instruct](https://tokenmargin.dev/models/qwen-2-5-72b-instruct-pricing-calculator.html?ref=github)** | `qwen/qwen-2.5-72b-instruct` | DeepInfra | **$0.12** | **$0.39** | $0.06 | 33K |
| **[NVIDIA Nemotron 70B Instruct](https://tokenmargin.dev/models/llama-3-1-nemotron-70b-instruct-pricing-calculator.html?ref=github)** | `nvidia/llama-3.1-nemotron-70b-instruct` | DeepInfra | **$0.12** | **$0.3** | $0.06 | 131K |
| **[Nex-N2.6](https://tokenmargin.dev/models/nex-n2-6-pricing-calculator.html?ref=github)** | `nex-agi/nex-n2.6` | Nex AGI | **$0.12** | **$0.4** | $0.024 | 262K |
| **[MiMo-V2.6-Flash](https://tokenmargin.dev/models/mimo-v2-6-flash-pricing-calculator.html?ref=github)** | `xiaomi/mimo-v2.6-flash` | Xiaomi MiMo | **$0.14** | **$0.28** | $0.0028 | 1M |
| **[DeepSeek V4.1 Flash](https://tokenmargin.dev/models/deepseek-v4-1-flash-pricing-calculator.html?ref=github)** | `deepseek/deepseek-v4.1-flash` | DeepSeek | **$0.14** | **$0.42** | $0.0042 | 1M |
| **[GPT-4o Mini](https://tokenmargin.dev/models/gpt-4o-mini-pricing-calculator.html?ref=github)** | `openai/gpt-4o-mini` | OpenAI | **$0.15** | **$0.6** | $0.075 | 128K |
| **[MiniMax M3.1 Flash](https://tokenmargin.dev/models/minimax-m3-1-flash-pricing-calculator.html?ref=github)** | `minimax/minimax-m3.1-flash` | MiniMax | **$0.15** | **$0.6** | $0.015 | 1M |
| **[Nemotron 3.5 Super VL](https://tokenmargin.dev/models/nemotron-3-5-super-vl-pricing-calculator.html?ref=github)** | `nvidia/nemotron-3.5-super-vl` | NVIDIA | **$0.15** | **$0.5** | $0.02 | 1M |
| **[Qwen3.8 Omni Flash](https://tokenmargin.dev/models/qwen3-8-omni-flash-pricing-calculator.html?ref=github)** | `qwen/qwen3.8-omni-flash` | Alibaba Qwen | **$0.15** | **$0.47** | $0.016 | 1M |
| **[Qwen3.8 Flash](https://tokenmargin.dev/models/qwen3-8-flash-pricing-calculator.html?ref=github)** | `qwen/qwen3.8-flash` | Alibaba Qwen | **$0.15** | **$0.47** | $0.016 | 1M |
| **[Llama 4 Maverick (17B-128E MoE)](https://tokenmargin.dev/models/llama-4-maverick-pricing-calculator.html?ref=github)** | `meta-llama/llama-4-maverick` | DeepInfra | **$0.19** | **$0.49** | $0.095 | 524K |
| **[DeepSeek R1 Distill Llama 70B](https://tokenmargin.dev/models/deepseek-r1-distill-llama-70b-pricing-calculator.html?ref=github)** | `deepseek/deepseek-r1-distill-llama-70b` | Groq | **$0.23** | **$0.69** | $0.11 | 131K |
| **[DeepSeek V3 (0324)](https://tokenmargin.dev/models/deepseek-chat-v3-0324-pricing-calculator.html?ref=github)** | `deepseek/deepseek-chat-v3-0324` | DeepInfra | **$0.24** | **$0.79** | $0.07 | 164K |
| **[Kimi K3.1 Pro](https://tokenmargin.dev/models/kimi-k3-1-pro-pricing-calculator.html?ref=github)** | `moonshotai/kimi-k3.1-pro` | Moonshot AI | **$0.2403** | **$8.402** | $0.2 | 1M |
| **[Claude 3 Haiku](https://tokenmargin.dev/models/claude-3-haiku-pricing-calculator.html?ref=github)** | `anthropic/claude-3-haiku` | Anthropic | **$0.25** | **$1.25** | $0.03 | 200K |
| **[GPT-5 Mini](https://tokenmargin.dev/models/gpt-5-mini-pricing-calculator.html?ref=github)** | `openai/gpt-5-mini` | OpenAI | **$0.25** | **$2** | $0.025 | 400K |
| **[Gemini 2.5 Flash](https://tokenmargin.dev/models/gemini-2-5-flash-pricing-calculator.html?ref=github)** | `google/gemini-2.5-flash` | Google | **$0.3** | **$2.5** | $0.03 | 1M |
| **[Mistral Codestral 2501](https://tokenmargin.dev/models/codestral-2501-pricing-calculator.html?ref=github)** | `mistralai/codestral-2501` | OpenRouter | **$0.3** | **$0.9** | $0.15 | 262K |
| **[Inkling 2 Small](https://tokenmargin.dev/models/inkling-2-small-pricing-calculator.html?ref=github)** | `thinkingmachines/inkling-2-small` | Thinking Machines | **$0.3** | **$1** | $0.03 | 1M |
| **[Command A+](https://tokenmargin.dev/models/command-a-plus-pricing-calculator.html?ref=github)** | `cohere/command-a-plus` | Cohere | **$0.3** | **$1.5** | $0.15 | 192K |
| **[Llama 3.2 90B Vision Instruct](https://tokenmargin.dev/models/llama-3-2-90b-vision-instruct-pricing-calculator.html?ref=github)** | `meta-llama/llama-3.2-90b-vision-instruct` | DeepInfra | **$0.35** | **$0.4** | $0.18 | 131K |
| **[GPT-4.1 Mini (75% Cache Discount)](https://tokenmargin.dev/models/gpt-4-1-mini-pricing-calculator.html?ref=github)** | `openai/gpt-4.1-mini` | OpenAI | **$0.4** | **$1.6** | $0.1 | 1M |
| **[Hy4](https://tokenmargin.dev/models/hy4-pricing-calculator.html?ref=github)** | `tencent/hy4` | Tencent Hunyuan | **$0.417** | **$1.25** | $0.021 | 1M |
| **[MiMo-V2.6-Pro](https://tokenmargin.dev/models/mimo-v2-6-pro-pricing-calculator.html?ref=github)** | `xiaomi/mimo-v2.6-pro` | Xiaomi MiMo | **$0.435** | **$0.87** | $0.0036 | 1M |
| **[DeepSeek R1 (671B Reasoning)](https://tokenmargin.dev/models/deepseek-r1-pricing-calculator.html?ref=github)** | `deepseek/deepseek-r1` | DeepInfra | **$0.5** | **$2.15** | $0.14 | 164K |
| **[Seed 2.1 Turbo](https://tokenmargin.dev/models/seed-2-1-turbo-pricing-calculator.html?ref=github)** | `bytedance-seed/seed-2-1-turbo` | ByteDance Seed | **$0.5** | **$2.5** | $0.25 | 262K |
| **[Mistral Large 4](https://tokenmargin.dev/models/mistral-large-4-0-pricing-calculator.html?ref=github)** | `mistralai/mistral-large-4-0` | Mistral AI | **$0.7** | **$2.1** | $0.07 | 1M |
| **[Claude 3.5 Haiku](https://tokenmargin.dev/models/claude-3-5-haiku-pricing-calculator.html?ref=github)** | `anthropic/claude-3.5-haiku` | Anthropic | **$0.8** | **$4** | $0.08 | 200K |
| **[Llama 3.1 405B Instruct](https://tokenmargin.dev/models/llama-3-1-405b-instruct-pricing-calculator.html?ref=github)** | `meta-llama/llama-3.1-405b-instruct` | DeepInfra | **$0.8** | **$0.8** | $0.4 | 131K |
| **[Amazon Nova Pro v1](https://tokenmargin.dev/models/nova-pro-v1-pricing-calculator.html?ref=github)** | `amazon/nova-pro-v1` | OpenRouter | **$0.8** | **$3.2** | $0.2 | 300K |
| **[Gemini 3.8 Flash](https://tokenmargin.dev/models/gemini-3-8-flash-pricing-calculator.html?ref=github)** | `google/gemini-3.8-flash` | Google | **$0.825** | **$4.125** | $0.0825 | 1M |
| **[GPT-6.1 Terra Pro](https://tokenmargin.dev/models/gpt-6-1-terra-pro-pricing-calculator.html?ref=github)** | `openai/gpt-6.1-terra-pro` | OpenAI | **$1** | **$5** | $0.05 | 1M |
| **[GPT-6.1 Terra](https://tokenmargin.dev/models/gpt-6-1-terra-pricing-calculator.html?ref=github)** | `openai/gpt-6.1-terra` | OpenAI | **$1** | **$5** | $0.05 | 1M |
| **[Inkling](https://tokenmargin.dev/models/inkling-pricing-calculator.html?ref=github)** | `thinkingmachines/inkling` | Thinking Machines | **$1** | **$4.05** | $0.17 | 524K |
| **[Hermes 4 405B](https://tokenmargin.dev/models/hermes-4-405b-pricing-calculator.html?ref=github)** | `nousresearch/hermes-4-405b` | Nous Research | **$1** | **$3** | $0.2 | 131K |
| **[OpenAI o3-mini](https://tokenmargin.dev/models/o3-mini-pricing-calculator.html?ref=github)** | `openai/o3-mini` | OpenAI | **$1.1** | **$4.4** | $0.55 | 200K |
| **[OpenAI o1-mini](https://tokenmargin.dev/models/o1-mini-pricing-calculator.html?ref=github)** | `openai/o1-mini` | OpenAI | **$1.1** | **$4.4** | $0.55 | 128K |
| **[ERNIE-Light-DT-1.0](https://tokenmargin.dev/models/ernie-light-dt-1-0-intl-pricing-calculator.html?ref=github)** | `baidu/ernie-light-dt-1.0-intl` | Baidu ERNIE | **$1.13** | **$3.94** | $0.113 | 1M |
| **[Gemini 2.5 Pro](https://tokenmargin.dev/models/gemini-2-5-pro-preview-03-25-pricing-calculator.html?ref=github)** | `google/gemini-2.5-pro-preview-03-25` | Google | **$1.25** | **$10** | $0.31 | 1M |
| **[Gemini 1.5 Pro (2M Context)](https://tokenmargin.dev/models/gemini-1-5-pro-pricing-calculator.html?ref=github)** | `google/gemini-1.5-pro` | Google | **$1.25** | **$5** | $0.3125 | 2M |
| **[Muse Spark Open](https://tokenmargin.dev/models/muse-spark-open-pricing-calculator.html?ref=github)** | `meta/muse-spark-open` | Meta AI | **$1.25** | **$4.25** | $0.15 | 1M |
| **[GPT-5](https://tokenmargin.dev/models/gpt-5-pricing-calculator.html?ref=github)** | `openai/gpt-5` | OpenAI | **$1.25** | **$10** | $0.125 | 400K |
| **[Qwen4 Max](https://tokenmargin.dev/models/qwen4-max-pricing-calculator.html?ref=github)** | `qwen/qwen4-max` | Alibaba Qwen | **$1.425** | **$4.275** | $0.0713 | 1M |
| **[Gemini 4 Hydrogen](https://tokenmargin.dev/models/gemini-4-hydrogen-pricing-calculator.html?ref=github)** | `google/gemini-4-hydrogen` | Google | **$1.5** | **$7.5** | $0.075 | 1M |
| **[Gemini Omni 1.2 Flash](https://tokenmargin.dev/models/gemini-omni-1-2-flash-pricing-calculator.html?ref=github)** | `google/gemini-omni-1.2-flash` | Google | **$1.5** | **$9** | $0.375 | 131K |
| **[Qwen 2.5 Max (Frontier MoE)](https://tokenmargin.dev/models/qwen-max-pricing-calculator.html?ref=github)** | `qwen/qwen-max` | OpenRouter | **$1.6** | **$6.4** | $0.8 | 131K |
| **[GLM 5.3 Prime](https://tokenmargin.dev/models/glm-5-3-prime-pricing-calculator.html?ref=github)** | `z-ai/glm-5.3-prime` | Z.ai (GLM) | **$1.68** | **$5.28** | $0.336 | 1M |
| **[OpenAI o3 (Frontier Reasoning)](https://tokenmargin.dev/models/o3-pricing-calculator.html?ref=github)** | `openai/o3` | OpenAI | **$2** | **$8** | $0.5 | 200K |
| **[Mistral Large 2 (2411)](https://tokenmargin.dev/models/mistral-large-2411-pricing-calculator.html?ref=github)** | `mistralai/mistral-large-2411` | OpenRouter | **$2** | **$6** | $1 | 131K |
| **[xAI Grok 2 (1212)](https://tokenmargin.dev/models/grok-2-1212-pricing-calculator.html?ref=github)** | `x-ai/grok-2-1212` | OpenRouter | **$2** | **$10** | $0.5 | 131K |
| **[xAI Grok 2 Vision](https://tokenmargin.dev/models/grok-2-vision-1212-pricing-calculator.html?ref=github)** | `x-ai/grok-2-vision-1212` | OpenRouter | **$2** | **$10** | $0.5 | 33K |
| **[Perplexity Sonar Reasoning Pro](https://tokenmargin.dev/models/sonar-reasoning-pro-pricing-calculator.html?ref=github)** | `perplexity/sonar-reasoning-pro` | OpenRouter | **$2** | **$8** | $1 | 128K |
| **[GPT-4.1 (1M Context Frontier)](https://tokenmargin.dev/models/gpt-4-1-pricing-calculator.html?ref=github)** | `openai/gpt-4.1` | OpenAI | **$2** | **$8** | $0.5 | 1M |
| **[Mistral Pixtral Large (124B Vision)](https://tokenmargin.dev/models/pixtral-large-2411-pricing-calculator.html?ref=github)** | `mistralai/pixtral-large-2411` | OpenRouter | **$2** | **$6** | $1 | 131K |
| **[Gemini 4 Carbon](https://tokenmargin.dev/models/gemini-4-carbon-pricing-calculator.html?ref=github)** | `google/gemini-4-carbon` | Google | **$2** | **$10** | $0.1 | 1M |
| **[Gemini 4 Argon](https://tokenmargin.dev/models/gemini-4-argon-pricing-calculator.html?ref=github)** | `google/gemini-4-argon` | Google | **$2** | **$10** | $0.1 | 1M |
| **[GPT-6.1 Sol Pro](https://tokenmargin.dev/models/gpt-6-1-sol-pro-pricing-calculator.html?ref=github)** | `openai/gpt-6.1-sol-pro` | OpenAI | **$2** | **$10** | $0.1 | 1M |
| **[GPT-6.1 Sol](https://tokenmargin.dev/models/gpt-6-1-sol-pricing-calculator.html?ref=github)** | `openai/gpt-6.1-sol` | OpenAI | **$2** | **$10** | $0.1 | 1M |
| **[Claude Sonnet 5.5](https://tokenmargin.dev/models/claude-sonnet-5-5-pricing-calculator.html?ref=github)** | `anthropic/claude-sonnet-5.5` | Anthropic | **$2** | **$10** | $0.1 | 1M |
| **[Grok 4.7](https://tokenmargin.dev/models/grok-4-7-pricing-calculator.html?ref=github)** | `x-ai/grok-4.7` | xAI | **$2** | **$6** | $0.5 | 500K |
| **[Fugu Max](https://tokenmargin.dev/models/fugu-max-pricing-calculator.html?ref=github)** | `sakana/fugu-max` | Sakana AI | **$2** | **$6** | $0.25 | 1M |
| **[Qwen3.8 2.4T A95B](https://tokenmargin.dev/models/qwen3-8-2-4t-a95b-pricing-calculator.html?ref=github)** | `qwen/qwen3.8-2.4t-a95b` | Alibaba Qwen | **$2** | **$6** | $0.25 | 1M |
| **[Claude Sonnet 5](https://tokenmargin.dev/models/claude-sonnet-5-pricing-calculator.html?ref=github)** | `anthropic/claude-sonnet-5` | Anthropic | **$2** | **$10** | $0.2 | 1M |
| **[Sonar Deep Research](https://tokenmargin.dev/models/sonar-deep-research-pricing-calculator.html?ref=github)** | `perplexity/sonar-deep-research` | Perplexity | **$2** | **$8** | $1 | 128K |
| **[GPT-4o](https://tokenmargin.dev/models/gpt-4o-pricing-calculator.html?ref=github)** | `openai/gpt-4o` | OpenAI | **$2.5** | **$10** | $1.25 | 128K |
| **[Cohere Command A (Enterprise RAG)](https://tokenmargin.dev/models/command-a-pricing-calculator.html?ref=github)** | `cohere/command-a` | OpenRouter | **$2.5** | **$10** | $1.25 | 256K |
| **[Cohere Command R+ (08-2024)](https://tokenmargin.dev/models/command-r-plus-08-2024-pricing-calculator.html?ref=github)** | `cohere/command-r-plus-08-2024` | OpenRouter | **$2.5** | **$10** | $1.25 | 128K |
| **[GPT-5.4](https://tokenmargin.dev/models/gpt-5-4-pricing-calculator.html?ref=github)** | `openai/gpt-5.4` | OpenAI | **$2.5** | **$15** | $0.25 | 1M |
| **[Claude Sonnet 4](https://tokenmargin.dev/models/claude-sonnet-4-pricing-calculator.html?ref=github)** | `anthropic/claude-sonnet-4` | Anthropic | **$3** | **$15** | $0.3 | 200K |
| **[Claude 3.7 Sonnet](https://tokenmargin.dev/models/claude-3-7-sonnet-pricing-calculator.html?ref=github)** | `anthropic/claude-3.7-sonnet` | Anthropic | **$3** | **$15** | $0.3 | 200K |
| **[Claude 3.7 Sonnet (Extended Thinking)](https://tokenmargin.dev/models/claude-3-7-sonnet-thinking-pricing-calculator.html?ref=github)** | `anthropic/claude-3.7-sonnet:thinking` | Anthropic | **$3** | **$15** | $0.3 | 200K |
| **[Claude 3.5 Sonnet (v2)](https://tokenmargin.dev/models/claude-3-5-sonnet-pricing-calculator.html?ref=github)** | `anthropic/claude-3.5-sonnet` | Anthropic | **$3** | **$15** | $0.3 | 200K |
| **[Sonar Pro Search](https://tokenmargin.dev/models/sonar-pro-search-pricing-calculator.html?ref=github)** | `perplexity/sonar-pro-search` | Perplexity | **$3** | **$15** | $1.5 | 200K |
| **[Claude Sonnet 4.5](https://tokenmargin.dev/models/claude-sonnet-4-5-pricing-calculator.html?ref=github)** | `anthropic/claude-sonnet-4.5` | Anthropic | **$3** | **$15** | $0.3 | 1M |
| **[Muse Wonder](https://tokenmargin.dev/models/muse-wonder-pricing-calculator.html?ref=github)** | `meta/muse-wonder` | Meta AI | **$4** | **$20** | $0.2 | 1M |
| **[Qwen3.8 Max Prime](https://tokenmargin.dev/models/qwen3-8-max-prime-pricing-calculator.html?ref=github)** | `qwen/qwen3.8-max-prime` | Alibaba Qwen | **$4** | **$12** | $0.5 | 1M |
| **[Claude Opus 5.5](https://tokenmargin.dev/models/claude-opus-5-5-pricing-calculator.html?ref=github)** | `anthropic/claude-opus-5.5` | Anthropic | **$4** | **$20** | $0.2 | 1M |
| **[Fugu Ultra v2](https://tokenmargin.dev/models/fugu-ultra-v2-pricing-calculator.html?ref=github)** | `sakana/fugu-ultra-v2` | Sakana AI | **$5** | **$30** | $0.5 | 1M |
| **[Claude Opus 5](https://tokenmargin.dev/models/claude-opus-5-pricing-calculator.html?ref=github)** | `anthropic/claude-opus-5` | Anthropic | **$5** | **$25** | $0.5 | 1M |
| **[GPT-5.5](https://tokenmargin.dev/models/gpt-5-5-pricing-calculator.html?ref=github)** | `openai/gpt-5.5` | OpenAI | **$5** | **$30** | $0.5 | 1M |
| **[Claude Fable 5.2](https://tokenmargin.dev/models/claude-fable-5-2-pricing-calculator.html?ref=github)** | `anthropic/claude-fable-5.2` | Anthropic | **$8** | **$40** | $0.2 | 1M |
| **[GPT-4 Turbo (Legacy)](https://tokenmargin.dev/models/gpt-4-turbo-pricing-calculator.html?ref=github)** | `openai/gpt-4-turbo` | OpenAI | **$10** | **$30** | $5 | 128K |
| **[GPT-6 Astra Pro](https://tokenmargin.dev/models/gpt-6-astra-pro-pricing-calculator.html?ref=github)** | `openai/gpt-6-astra-pro` | OpenAI | **$10** | **$50** | $1 | 1M |
| **[Claude 3 Opus (Legacy High-Cost)](https://tokenmargin.dev/models/claude-3-opus-pricing-calculator.html?ref=github)** | `anthropic/claude-3-opus` | Anthropic | **$15** | **$75** | $1.5 | 200K |
| **[OpenAI o1 (Frontier Reasoning)](https://tokenmargin.dev/models/o1-pricing-calculator.html?ref=github)** | `openai/o1` | OpenAI | **$15** | **$60** | $7.5 | 200K |
| **[GPT-4 32k (Deprecated Legacy)](https://tokenmargin.dev/models/gpt-4-32k-pricing-calculator.html?ref=github)** | `openai/gpt-4-32k` | OpenAI | **$60** | **$120** | $30 | 33K |
| **[GPT-4.5 Preview (Cost Trap Alert)](https://tokenmargin.dev/models/gpt-4-5-preview-pricing-calculator.html?ref=github)** | `openai/gpt-4.5-preview` | OpenAI | **$75** | **$150** | $37.5 | 128K |

---

## License

MIT — Maintained by **[TokenMargin.dev](https://tokenmargin.dev/?ref=github)**.
