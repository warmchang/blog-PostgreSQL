# Workflows

Use these repeatable workflows to produce stable, verifiable output.

## PostgreSQL/PolarDB Technical Answer

1. Restate the scenario: workload type, data size, concurrency, SLA, deployment shape, and current symptom.
2. Search blog evidence by category and keyword.
3. Explain the mechanism before the fix: storage, index, optimizer, MVCC, lock, WAL, replication, memory, IO, or network.
4. Provide the practical path:
   - immediate mitigation
   - root-cause confirmation
   - durable design or configuration change
   - regression guard
5. Include SQL/commands where possible.
6. State assumptions and when the recommendation fails.

Output skeleton:

```markdown
## 结论
## 判断依据
## 排查/实施步骤
## SQL或命令
## 风险与回滚
## 验收标准
## 参考
```

## Performance Diagnosis

Order checks by probability and reversibility:

1. Confirm symptom: latency, QPS/TPS, CPU, IO, locks, bloat, checkpoint, WAL, autovacuum, network, connection count.
2. Find top SQL: `pg_stat_statements`, slow log, `auto_explain`, `EXPLAIN (ANALYZE, BUFFERS)`.
3. Check plan mismatch: wrong row estimate, missing/unused index, correlation, stale stats, parameter sensitivity.
4. Check memory and temp files: `work_mem`, hash/sort spill, parallelism, connection fan-out.
5. Check MVCC maintenance: dead tuples, autovacuum lag, freeze, bloat.
6. Check contention: row locks, relation locks, LWLock, IO queue, WAL sync.
7. Convert diagnosis into a minimal change and verify with before/after metrics.

Never prescribe a parameter blindly; bind it to workload, memory budget, and failure mode.

## Evidence Pack

Before giving a non-trivial answer, collect enough evidence to avoid overfitting to one post:

1. Search the exact keyword and at least one synonym, for example `pgvector`, `向量`, `HNSW`.
2. Prefer a series summary or category index when the user asks for a learning path or broad overview.
3. Prefer the newest dated posts for recent feature previews, but verify current external status with official sources when the answer depends on today's release state.
4. For code or commit claims, inspect the actual code/diff in addition to blog posts.
5. Cite repository-relative paths in the final answer.

Use JSON output when the search result is passed into another tool:

```bash
python3 skills/digoal/scripts/search_blog.py "pgvector" --json --limit 5
```

## Architecture and Selection

Start from first principles:

- What value must the database protect or accelerate?
- What is the dominant access pattern: OLTP, OLAP, HTAP, search, vector, graph, GIS, time-series, stream?
- What are scale dimensions: data volume, write rate, read rate, retention, tenant count, region count?
- What are hard constraints: RPO/RTO, consistency, compliance, cost, team skill, ecosystem?
- What failure mode is unacceptable?

Compare options with a table: `方案`, `适合场景`, `代价`, `风险`, `验证方法`.

## Article Writing in digoal Style

Use when asked to create public-account articles, project interpretations, course notes, or technical explainers.

Before drafting:

1. Think through the writing framework first: target reader, core thesis, article type, section order, expected evidence, practical path, and caveats.
2. Search source material after the framework is clear.
3. Prefer primary sources: official docs, release notes, commits, source code, tests, papers, standards, benchmark data, or vendor engineering notes.
4. For GitHub open-source projects, use DeepWiki MCP when available to read the repo wiki/structure and ask repo-grounded questions; treat it as a fast project-understanding layer, then verify important claims against upstream docs, source code, commits, or tests.
5. Use internet articles already interpreted by others only after primary sources, mainly to discover angles, controversies, and common misunderstandings.
6. Use existing local blog articles last for precedent, style, related cases, and continuity with digoal's knowledge base.
7. Digest the collected context before writing: separate verified facts, reasonable inferences, uncertain claims, reusable examples, and claims that must be removed or softened.
8. Start drafting only when the context can support the thesis, mechanism explanation, hands-on method, effect verification, and boundary conditions.

Hard gate: for a technical article about an external technology or open-source project, a context pack that only contains local blog search results is insufficient. Stop and gather upstream primary sources first. If upstream access, internet search, or DeepWiki MCP is unavailable, report the limitation and ask whether the user wants a blog-only draft with explicit caveats.

Authority order for source material:

1. Upstream source code, commit diff, tests, release notes, official docs, standards/specs, or peer-reviewed paper.
2. Vendor engineering blog or maintainer-authored design note.
3. DeepWiki MCP for GitHub repos, used for repo navigation, architecture understanding, and question answering.
4. Reproducible benchmark, lab, SQL, command output, or test result.
5. Reputable third-party technical articles, used as secondary interpretation only.
6. Existing local blog articles, used for precedent, style, historical continuity, and related cases.

Most authoritative sites depend on the topic:

- PostgreSQL: `postgresql.org` docs, `git.postgresql.org` or upstream GitHub mirror commits, mailing list archives, source code, and tests.
- DuckDB: `duckdb.org` docs/release notes, `github.com/duckdb/duckdb`, source code, tests, and extension docs.
- Lance: official Lance docs/site, `github.com/lancedb/lance`, source code, tests, issues/PRs, release notes, and related Apache Arrow/DataFusion docs when the claim depends on those layers.
- Open-source projects in general: upstream project docs, GitHub/GitLab repo, maintainer release notes, code, tests, design docs, issues, PRs, and official benchmarks.
- Cloud/vendor products: official docs, release notes, SLA/pricing pages, product blogs by the vendor engineering team, and public benchmark methodology.
- Academic algorithms or systems: original paper, authors' artifact/repo, conference proceedings, and reproducibility reports.

Drafting steps:

1. Pick a sharp title that names the consequence, not just the feature.
2. Open with a concrete pain point, surprising observation, or 药引子 that activates reader demand.
3. State the core judgment early, preferably as a falsifiable thesis.
4. Explain from mechanism or first principles.
5. Add evidence: official docs, code, benchmark, case, before/after comparison, or blog precedent.
6. Pair theory with practice: mechanism plus SQL/commands/config/checklist.
7. Explain the effect: what improves, through which path, and how to measure it.
8. Add caveats: what assumptions must hold and what happens if they fail.
9. Close with a short takeaway, action suggestion, or "你怎么看" interaction when publishing style is requested.

Sections for PG commit/new feature interpretation:

```markdown
# 标题
## 摘要
关键词:
背景痛点:
核心价值:
## 原理介绍
## 应用场景及最佳实践
## 风险、限制与版本注意
## 小结和思考
## 参考
```

Article type templates:

### PG Commit or New Feature Interpretation

```markdown
# 标题
## 摘要
关键词:
背景痛点:
核心价值:
## 药引子: 为什么这个变化值得看
## 过去怎么做, 痛在哪里
## 这次改了什么
## 第一性原理: 为什么这样设计
## 原理介绍: 结合代码/commit讲清楚机制
## 应用场景及最佳实践
## 怎么验证: SQL、命令、指标或测试
## 风险、限制与版本注意
## 小结和思考
## 参考
```

### Product or Architecture Selection

```markdown
# 标题
## 结论先行
## 药引子: 为什么现在必须重新判断
## 场景和约束
## 错误选型方式
## 第一性原理: 真正要优化的底层变量
## 选择标准
## 方案对比
## 落地路径
## 风险边界和替代方案
## 推荐动作
## 参考
```

### 德说 or Strategic Analysis

```markdown
# 标题
## 现象
## 反常识判断
## 底层变量: 供需、成本、效率、信任、生态或飞轮
## 为什么会这样
## 案例或证据托底
## 对个人/团队/企业意味着什么
## 前提条件
## 如果前提崩塌, 结论怎么换
## 行动建议
```

Pre-publish checks:

- Does the article turn a single case into a universal conclusion?
- Does every core judgment have a source, case, code path, benchmark, or reproducible check?
- Does it explain the mechanism behind the claimed effect?
- Does it give the reader an operational next step?
- Does it state the premise and the alternative view when the premise fails?
- Does any sentence claim certainty that the evidence cannot support?

Post-draft validation:

1. Extract the article's factual claims: version numbers, feature behavior, API names, SQL syntax, configuration names, performance claims, architecture diagrams, and causal explanations.
2. Check each claim against the highest-authority available source. Use official docs/release notes for documented behavior, source code/commits/tests for implementation behavior, standards/papers for algorithmic claims, and DeepWiki MCP for repo-grounded cross-checking on open-source projects.
3. Run reproducible checks when feasible: SQL examples, CLI commands, unit tests, benchmark snippets, `EXPLAIN`, configuration inspection, or source grep.
4. Mark unsupported claims as inference, soften them, or remove them.
5. Verify terminology consistency: project name, version, extension name, file path, function name, catalog/view name, and metric name.
6. Verify boundaries: when the recommendation works, when it fails, how to rollback, and what metric proves success.
7. Re-read the final article once from the target reader's perspective: DBA, architect, developer, product owner, or learner.

Validation output should be explicit when the user asks for review:

```markdown
## 校验结论
## 已核实的关键事实
## 仍需谨慎的推断
## 修改或弱化的表述
## 参考来源
```

## Source Code or Commit Interpretation

1. Inspect the exact commit, diff, tests, docs, and nearby code.
2. Separate "what changed" from "why it matters".
3. Translate internals for the target reader: DBA, developer, architect, or product manager.
4. Avoid unsupported performance claims unless benchmark or code path proves them.
5. Verify article claims against code before final output.
6. If writing multiple files, keep each topic in an independent context and avoid cross-contamination.

## AI Skill/Digital Employee Distillation

Use the framework from `202603/20260317_03.md`, `202603/20260319_05.md`, and `202603/20260324_06.md`.

For each skill, define:

- Trigger: when should it be used?
- Input contract: what information is required?
- Decision path: how does it choose a workflow?
- Tools: what files, MCPs, CLIs, scripts, or source systems are used?
- Validation: how is correctness checked?
- Fallback: what happens when evidence is missing or tool calls fail?
- Output template: what artifact is produced?
- Responsibility boundary: what the skill must not do.

Strong skill criteria:

- 可验证: output can be checked.
- 可复用: procedure works repeatedly.
- 可规模化: not dependent on one-off genius.
- 可追责: inputs, steps, and boundaries are clear.

## Community and Ecosystem Strategy

Use digoal's community/product background when asked about open-source growth, database product promotion, or developer ecosystem.

Frame with:

- User pain and adoption barrier.
- Product core value and differentiated scenario.
- Content system: tutorials, labs, cases, benchmarks, migration guides, best practices.
- Community mechanism: contributors, users, partners, training, events, support channels.
- Flywheel: content -> trust -> usage -> feedback -> cases -> ecosystem.
- Metrics: users, deployments, contributors, issues, stars, courses, conversions, enterprise references.

Avoid vanity metrics without tying them to adoption or business value.
