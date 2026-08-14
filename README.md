# Workspace Booking Debug Lab

会議室・設備予約、承認、取消、外部カレンダー同期を題材にしたReact / Go / FastAPIのデバッグ教材です。React画面、Go Gateway、FastAPI、PostgreSQL、Redis、WireMock、Kubernetesをまたいで、観測、仮説、最小修正、回帰テストを練習します。

| コマンド | 用途 |
| --- | --- |
| `pnpm install` | Webの依存関係を導入する。 |
| `./scripts/verify.sh` | TypeScript、Go、Python、文書、差分を検証する。 |
| `docker compose up --build` | フルスタックを起動する。 |

`docs/issues/`から問題を選び、対応するバグ導入コミットに切り替えて調査します。`solutions/`は自分の修正とテストを作った後に参照してください。
