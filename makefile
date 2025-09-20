.PHONY: lint format typecheck test check

# 彩色输出（可选）
GREEN  := \033[0;32m
BLUE   := \033[0;34m
RESET  := \033[0m

lint:
	@echo "\n-------------------- Lint (ruff) --------------------"
	@uv run ruff check greenremover tests || (echo "Lint failed" && exit 1)
	@echo "$(GREEN)Lint passed$(RESET)\n"

format:
	@echo "\n-------------------- Format (black) --------------------"
	@uv run black greenremover tests
	@echo "$(GREEN)Format done$(RESET)\n"

typecheck:
	@echo "\n-------------------- Type Check (mypy) --------------------"
	@uv run mypy || (echo "Type check failed" && exit 1)
	@echo "$(GREEN)Type check passed$(RESET)\n"

test:
	@echo "\n-------------------- Tests (pytest) --------------------"
	@uv run pytest || (echo "Tests failed" && exit 1)
	@echo "$(GREEN)Tests passed$(RESET)\n"

check: lint typecheck test
	@echo "\n========================================================"
	@echo "$(GREEN)All checks passed!$(RESET)"
	@echo "========================================================\n"
