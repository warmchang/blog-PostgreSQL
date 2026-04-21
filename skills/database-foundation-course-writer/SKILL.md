---
name: database-foundation-course-writer
description: Write Chinese "数据库筑基课" Markdown articles for database architects, DBAs, and application developers. Use when the user provides a database foundation article title and references such as technical docs, product manuals, open-source repositories, DeepWiki pages, papers, source code, or related blog posts, and wants a rigorous, diagram-rich, practice-oriented article saved under the current project's markdown folder.
---

# Database Foundation Course Writer

## Overview

Write a publishable Chinese Markdown article in the "数据库筑基课" style. The article must help database architects, DBAs, and application developers understand the mechanism, tradeoffs, practice path, and operational boundaries of a database technology.

## Inputs

Require or infer:

- Article title.
- Reference materials: official docs, product manuals, source repositories, DeepWiki pages, papers, source code, existing local articles, SQL examples, benchmark data, or issue discussions.
- Target technology category: table storage, index structure, data type/operator, optimizer scan algorithm, execution operator, maintenance mechanism, or scenario practice.

If key references are missing, search primary sources first. Prefer official docs, source code, papers, and project README over secondary summaries.

## Output

Save the final Markdown article into the current project's `markdown` folder. Use a filename derived from the title when no filename is provided, or follow the repository's existing naming convention if obvious.

Do not save until the article has passed the validation checklist.

## Workflow

1. Parse the title and references.
2. Classify the topic as table storage, index structure, data type/operator, scan/execution algorithm, or scenario practice.
3. Read primary references and extract mechanisms, terminology, examples, limits, and source-backed claims.
4. Build the article around "background pain -> definition -> principle -> tradeoff -> comparison -> practice -> boundary".
5. Add diagrams using Markdown-compatible formats: Mermaid, ASCII layout, tables, or existing reference images when allowed.
6. Write runnable examples when possible. Never invent execution output.
7. Validate logic, examples, citations, and Markdown rendering.
8. Save the final Markdown file under `markdown`.

## Article Structure

Use this structure unless the topic strongly requires a different order.

```markdown
## 数据库筑基课 - <主题>

### 作者
digoal

### 日期
<YYYY-MM-DD>

### 标签
PostgreSQL , PolarDB , DuckDB , 应用开发者 , 数据库筑基课 , <分类标签>

----

## 背景
链接或引用数据库筑基课大纲。说明本节属于哪一类基础能力，并从业务或工程痛点切入。

## 一、它解决什么问题？
说明技术点出现的背景、原问题、传统做法的不足、转化后的问题，以及牺牲的代价。

## 二、它是什么？
给出简洁定义，解释逻辑模型、物理模型、关键术语和适用层次。

## 三、核心原理
解释内部结构、关键算法、数据布局、读写路径、生命周期、复杂度、维护机制。

## 四、横向对比
和竞品、相邻技术或不同实现比较，并解释原因。

## 五、效果如何？
说明收益和代价，例如 IO、block/page、压缩比、延迟、吞吐、召回率、误判率、读写空间放大。

## 六、实操 DEMO
给出最小可验证实验、SQL、配置、EXPLAIN 或同类验证。无法执行时明确说明。

## 七、最佳实践
分别面向数据库架构师、DBA、业务开发者给出推荐做法、原因、风险和验证方式。

## 八、适合与不适合场景
绑定 workload 写清楚适合和不适合的原因。

## 九、常见坑
列出真实工程风险和规避方法。

## 十、扩展问题
提出能帮助读者迁移到其他技术的思考题。

## 十一、扩展阅读
列出官方文档、论文、源码、DeepWiki、项目 README、已有相关文章和高质量二手资料。
```

## Topic Guidance

For table storage topics, cover file/page/block/row/column layout, insert/update/delete/read, MVCC or visibility, vacuum/compaction, compression, encoding, cold storage, and read/write/space amplification.

For index topics, cover data organization, build, insert, delete, update, vacuum/merge, search/scan algorithm, complexity, space cost, recall or false positives, and how the optimizer/executor uses the index.

For data type and operator topics, cover representation, operator semantics, index support, selectivity estimation, optimizer impact, and modeling patterns.

For scan and execution topics, cover seq scan, index scan, index only scan, bitmap scan, skip scan, sampling, joins, sort, aggregate, CTE, subquery, parallelism, JIT, vectorized execution, cost model, statistics, memory/disk behavior, and EXPLAIN verification.

For scenario practice topics, cover business model, schema, indexes, partitions, hot/cold split, SQL, bottleneck diagnosis, observability, and evolution path.

## Comparison Table

Use a comparison table when there are meaningful alternatives.

| 维度 | 本文技术 | 对比技术 A | 对比技术 B |
| --- | --- | --- | --- |
| 主要目标 |  |  |  |
| 写入代价 |  |  |  |
| 读取代价 |  |  |  |
| 空间成本 |  |  |  |
| 事务/MVCC |  |  |  |
| 适合场景 |  |  |  |
| 不适合场景 |  |  |  |

Explain the reasons behind the table. Do not only list conclusions.

## Style Rules

Write in Chinese.

Use a direct, practical technical style:

- Start from concrete business pain.
- Explain mechanisms from first principles.
- Use analogies only when they reduce cognitive cost.
- Prefer "为什么、怎么做、代价是什么、怎么验证" over abstract description.
- Be explicit about tradeoffs and limitations.

Every diagram must explain structure, flow, comparison, or decision logic. Avoid decorative diagrams.

## Source Handling

When references include source code, inspect relevant files instead of relying only on README text.

When references include papers, extract the algorithm, assumptions, limitations, and evaluation conditions.

When references include DeepWiki, use it to understand architecture, then verify important claims against source code or official docs when possible.

When references conflict, prefer primary sources and state the discrepancy.

## Validation Checklist

Before saving the final file, verify:

- The title matches the topic.
- The article links back to the database foundation course outline when available.
- The topic category is clear.
- Every major claim is backed by a source, code path, experiment, or clearly marked inference.
- Examples are syntactically correct.
- SQL examples are executable or explicitly marked as unexecuted.
- Performance numbers are not fabricated.
- Tradeoffs include both benefits and costs.
- Suitable and unsuitable scenarios are concrete.
- Cross-product comparison is technically fair.
- Terminology is consistent.
- Markdown renders correctly.
- Mermaid diagrams are valid.
- The final article is saved under the current project's `markdown` folder.

## Final Response

After saving the Markdown file, reply with:

- Saved file path.
- Main sources used.
- Whether examples were executed.
- Any unresolved uncertainty.
