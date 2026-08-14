# 観測ランブック

最初にReactのNetworkで`X-Request-Id`、リクエスト、応答を記録します。次にGo Gateway、FastAPI、外部カレンダーのログを同じIDで照合します。空き枠問題ではWireMockの受信内容、Redisの値・TTL、FastAPIのキャッシュヒットを確認します。競合や部分コミットでは、SQL、予約状態、監査記録、version、トランザクション境界を確認します。Kubernetes問題ではPodイベント、環境変数、Service名、readiness probeを確認します。
