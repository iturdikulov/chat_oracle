# Project To-Do and history

Roadmap:

1. **Phase 1 (MVP):** FastaPI + Pony ORM + Парсинг чата. Базовый поиск по ключевым словам. CLI для тестирования.
2. **Phase 2 (AI):** Интеграция Embeddings и векторного поиска. Реализация логики "Оракула".
3. **Phase 3 (Video):** Celery-воркеры с FFmpeg. Генерация простых отрывков.
4. **Phase 4 (UI):** Vue.js интерфейс, Pinia для трекинга задач, визуализация Heatmap.

Data ingestion: Download chat logs via API or scraping.
Storage: PostgreSQL (structured fields: user, timestamp, message, emotes).
Processing: Python (pandas, TensorFlow?).
Visualization: Plotly, Grafana, or a custom FastAPI dashboard.

## Phase 1: Project Setup & Infrastructure

- TODO: Better readme
- TODO: Init vue & flask instance
- TODO: Try to use devcontainers

## Phase 2: Database Layer, architecture

## Phase 3: Fetcher Module 

## Phase 4: Video Worker 

## Phase 5: FastAPI Server

## Phase 6: Vue Frontend

## Phase 7: Testing & Quality Assurance

- TODO: Initialize testing workflow

## Phase 8: Documentation & Deployment

## Analytics

### Chat

Overall stream health and community.

Break chat into time windows (e.g., 30s or 1min bins).
Measure message volume, sentiment, emote usage per window.
Detect recurring patterns (e.g., hype at start, lull in middle, spike at climax).
Skills: Time‑series analysis, window functions in SQL, visualization.

### Topic Modeling

What viewers are talking about during different segments.

Use NLP techniques like LDA or BERTopic on chat text.
Map topics to timestamps.
Compare topic shifts across streams or games.
Skills: NLP, clustering, dimensionality reduction.

### User Behavior Profiling

Different types of chat participants.

Cluster users by activity (lurkers, casual chatters, spammers, power users).
Track how user engagement changes across streams.
Build dashboards showing distribution of user types.
Skills: Clustering, user segmentation, behavioral analytics.

### Emote Burst Detection

Sudden surges in specific emotes (e.g., PogChamp).

Track frequency of each emote over time.
Detect bursts using statistical thresholds.
Correlate bursts with video events (kills, goals, jokes).
Skills: Event detection, anomaly detection, visualization.

### Cross‑Stream Comparative Analytics

How chat differs between streamers or games.

Compare average sentiment, emote usage, message length.
Identify unique “chat signatures” for each streamer.
Build similarity scores between communities.
Skills: Comparative statistics, similarity metrics, dashboards.

### Moderation & Toxicity Trends

What to analyze: How moderation interacts with chat flow.

Detect toxic language using classifiers.
Compare moderation events vs. toxic spikes.
Study effectiveness of moderation strategies.
Skills: NLP classification, ethics in data, correlation analysis.

### Predictive Modeling

What to analyze: Can chat predict future events?

Train models to predict hype moments based on chat features.
Predict streamer actions (e.g., big plays) from chat bursts.
Skills: Machine learning, feature engineering, supervised learning.
