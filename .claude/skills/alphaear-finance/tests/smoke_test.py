import sys
import tempfile
from pathlib import Path
from typing import Final

REPOSITORY_ROOT: Final[Path] = Path(__file__).resolve().parents[1]
SCRIPTS_DIRECTORY: Final[Path] = REPOSITORY_ROOT / "alphaear-finance" / "scripts"
sys.path.insert(0, str(SCRIPTS_DIRECTORY))

from core.database_manager import DatabaseManager
from core.stock_tools import EastMoneyDirect, StockTools
from deepear.deepear_lite import DeepEarLiteTools
from news.news_tools import NewsNowTools, PolymarketTools


def run_smoke_test() -> None:
    with tempfile.TemporaryDirectory(prefix="alphaear-finance-") as temporary_directory:
        database_path: Path = Path(temporary_directory) / "smoke.sqlite3"
        database = DatabaseManager(db_path=str(database_path))
        try:
            saved_count: int = database.save_daily_news(
                [
                    {
                        "id": "smoke-1",
                        "source": "smoke",
                        "rank": 1,
                        "title": "AlphaEar Finance smoke test",
                        "url": "https://example.com",
                        "content": "local-only validation",
                        "publish_time": None,
                        "meta_data": {},
                    }
                ]
            )
            stored_news: list[dict] = database.get_daily_news(source="smoke", limit=5, days=1)
            if saved_count != 1 or len(stored_news) != 1:
                raise RuntimeError(
                    f"SQLite smoke test failed: saved_count={saved_count}, stored_count={len(stored_news)}"
                )

            stock_tools = StockTools(database, auto_update=False)
            news_tools = NewsNowTools(database)
            polymarket_tools = PolymarketTools(database)
            if not isinstance(stock_tools, StockTools):
                raise TypeError("StockTools construction failed")
            if not isinstance(news_tools, NewsNowTools):
                raise TypeError("NewsNowTools construction failed")
            if not isinstance(polymarket_tools, PolymarketTools):
                raise TypeError("PolymarketTools construction failed")
            if not callable(EastMoneyDirect.fetch_kline):
                raise TypeError("EastMoneyDirect.fetch_kline is unavailable")
            if not callable(DeepEarLiteTools.fetch_latest_signals):
                raise TypeError("DeepEarLiteTools.fetch_latest_signals is unavailable")
        finally:
            database.close()


if __name__ == "__main__":
    run_smoke_test()
    print("AlphaEar Finance smoke test passed.")
