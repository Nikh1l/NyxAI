# Creator Dashboard Roadmap

## Vision

Build a Creator Dashboard inside the Nyx project that manages social
media interactions from a single interface.

### Initial Goal

-   Connect to Instagram using the Meta Graph API.
-   Synchronize reels and comments into a local SQLite database.
-   Display reels and comments in a React dashboard.
-   Later, use Ollama to generate AI-assisted replies for review before
    posting.

------------------------------------------------------------------------

# Architecture

``` text
                Nyx

          ┌──────────────────┐
          │  React Dashboard │
          └────────┬─────────┘
                   │
              FastAPI API
                   │
     ┌─────────────┼─────────────┐
     │             │             │
Instagram     YouTube       Future...
Connector     Connector
     │             │
     └─────────────┘
            Unified Social Layer
                   │
              SQLite/Postgres
                   │
            Ollama AI Services
```

------------------------------------------------------------------------

# Repository Layout

``` text
apps/
    creator_dashboard/
        frontend/
        backend/

core/
    social/
        base.py
        models.py

        instagram/
            auth.py
            client.py
            sync.py
            service.py

    storage/
        database.py
        models.py
        migrations/

configs/
    instagram.yml

tests/
    social/
```

------------------------------------------------------------------------

# Roadmap

## Phase 0 -- Foundation

Deliverables

-   Create project skeleton.
-   Scaffold React + Vite frontend.
-   Scaffold FastAPI backend.
-   Create reusable social connector layer.
-   Configure SQLite.
-   Add `/health` endpoint.

Success Criteria

-   React frontend loads.
-   FastAPI backend runs.
-   Frontend communicates with backend.

------------------------------------------------------------------------

## Phase 1 -- Meta Setup

Tasks

-   Create Meta Developer account.
-   Create Meta App.
-   Link Facebook Page.
-   Connect Instagram Creator account.
-   Enable Instagram Graph API.
-   Generate long-lived access token.
-   Verify API access using curl.

Success Criteria

-   Graph API returns reels.

------------------------------------------------------------------------

## Phase 2 -- Backend Skeleton

Endpoints

-   GET /health
-   POST /sync
-   GET /reels
-   GET /comments

Initially return mock data.

------------------------------------------------------------------------

## Phase 3 -- Database

Tables

-   Media
-   Comments
-   Replies
-   SyncLog

------------------------------------------------------------------------

## Phase 4 -- Instagram Client

Replace mocked data with Graph API integration.

------------------------------------------------------------------------

## Phase 5 -- Synchronization

Workflow

1.  Fetch reels.
2.  Store locally.
3.  Fetch comments.
4.  Store locally.

------------------------------------------------------------------------

## Phase 6 -- Dashboard

Pages

-   Dashboard
-   Reel Details
-   Settings

Features

-   Reel list
-   Comment list
-   Filters
-   Sync status

------------------------------------------------------------------------

## Phase 7 -- AI Assistance

Workflow

Comment → Classify → Generate draft → Human review → Save

------------------------------------------------------------------------

## Phase 8 -- Reply Posting

Workflow

Approve draft → Instagram API → Update local database

------------------------------------------------------------------------

# Immediate Next Task

Implement Phase 0 by:

1.  Creating the folder structure.
2.  Scaffolding FastAPI.
3.  Scaffolding React + Vite.
4.  Adding SQLite support.
5.  Creating the social connector interfaces.
6.  Verifying frontend ↔ backend communication.

After Phase 0 is complete, proceed with Meta integration.
