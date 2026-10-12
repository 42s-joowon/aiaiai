# 제출 가이드 & 학습 정리

코드와 커밋 기록은 저장소에 모두 들어 있습니다.
아래는 **내 PC에서 직접 해야 하는 작업**(개발 환경 설정, 스크린샷)과 과제 목표에 대한 정리입니다.

---

## 1. 개발 환경 설정 (스크린샷 ①)

VSCode 터미널(`` Ctrl+` ``)에서 순서대로 실행하고, 결과가 한 화면에 보이게 캡처합니다.

```bash
# Python 버전 확인 (3.10 이상)
python --version

# Hello 출력 확인
python hello.py

# Git 버전 확인
git --version

# Git 사용자 정보 / 기본 브랜치 설정
git config --global user.name "내 이름"
git config --global user.email "내 GitHub 이메일"
git config --global init.defaultBranch main

# 설정 확인
git config --global --list
```

VSCode에서 함께 확인할 것

- [ ] 확장(Extensions, `Ctrl+Shift+X`)에서 **Python** 설치 (Korean Language Pack은 선택)
- [ ] 왼쪽 아래 계정 아이콘 → **GitHub로 로그인** → 계정 이름이 보이는지 확인
- [ ] 소스 제어(`Ctrl+Shift+G`) 패널에서 저장소가 인식되는지 확인

> 스크린샷 예: Extensions 화면(Python 설치됨) + 터미널(버전/설정 출력) + 계정 메뉴(GitHub 로그인됨)

## 2. 내 PC로 내려받고 실행하기 (clone, pull)

```bash
# 저장소 복제 (clone)
git clone https://github.com/42s-joowon/aiaiai.git
cd aiaiai

# 원격 변경 사항 가져오기 (pull)
git pull origin main

# 실행
python prompt_manager.py
```

공개 샘플 저장소 clone 실습 (확인 후 삭제 가능)

```bash
cd ..
git clone https://github.com/octocat/Spoon-Knife.git
cd Spoon-Knife
ls              # Windows PowerShell은 dir
git log --oneline
cd .. && rm -rf Spoon-Knife
```

## 3. 프로그램 실행 결과 (스크린샷 ②)

아래 순서로 입력하면 필요한 화면을 모두 캡처할 수 있습니다.

| 순서 | 입력 | 캡처할 화면 |
|---|---|---|
| 1 | (실행 직후) | 메뉴 화면 |
| 2 | `1` → 제목/내용 입력 → 카테고리 `1` | 프롬프트 추가 |
| 3 | `2` | 프롬프트 목록 |
| 4 | `3` → `1` | 카테고리별 조회 |
| 5 | `4` → `블로그` | 프롬프트 검색 |
| 6 | `5` → `1` | 프롬프트 상세 보기 |
| 7 | `6` → `2` | 즐겨찾기 추가 |
| 8 | `7` | 즐겨찾기 목록 |
| 9 | `99` | 잘못된 번호 안내 |
| 10 | `0` | 종료 |

(보너스) `8` 수정, `9` 삭제, `10` TOP 5, `11`/`12` JSON 저장·불러오기, `13` Markdown 내보내기 화면도 함께 캡처하면 좋습니다.

## 4. Git 로그 (스크린샷 ③)

```bash
git log --oneline --graph
```

`feature/prompt-list`, `feature/bonus` 브랜치가 갈라졌다가 병합된 그래프가 보이면 됩니다.

## 5. 클라우드 환경에서 찍은 터미널 스크린샷

Claude Code 클라우드 환경의 터미널에서 실제로 명령어와 프로그램을 실행해 찍은 화면이 [`docs/screenshots/`](screenshots/)에 있습니다.

| 파일 | 내용 |
|---|---|
| [01_env.png](screenshots/01_env.png) | `python3 --version`, `hello.py` 실행, `git --version`, Git 사용자 정보·기본 브랜치(main), 원격 저장소 |
| [02_menu.png](screenshots/02_menu.png) | 메뉴 화면 |
| [03_add.png](screenshots/03_add.png) | 프롬프트 추가 |
| [04_list.png](screenshots/04_list.png) | 프롬프트 목록 |
| [05_category.png](screenshots/05_category.png) | 카테고리별 조회 |
| [06_search.png](screenshots/06_search.png) | 프롬프트 검색 |
| [07_detail.png](screenshots/07_detail.png) | 프롬프트 상세 보기 |
| [08_favorite.png](screenshots/08_favorite.png) | 즐겨찾기 추가 + 즐겨찾기 목록 |
| [09_invalid_exit.png](screenshots/09_invalid_exit.png) | 잘못된 번호 안내 + 종료 |
| [10_bonus.png](screenshots/10_bonus.png) | 보너스: 조회수 TOP 5, JSON 저장, Markdown 내보내기 |
| [11_git_log.png](screenshots/11_git_log.png) | `git log --oneline --graph` |

> 이 환경의 Git 사용자 정보는 클라우드 환경 기본값(Claude)이고, VSCode 화면(확장 설치, GitHub 로그인)은 클라우드 터미널에서 찍을 수 없습니다.
> 제출 규정상 **본인 PC의 VSCode 화면과 본인 Git 설정**이 필요하다면 1절 순서대로 직접 캡처해 교체하세요.

## 6. 제출물 체크리스트

- [ ] GitHub 저장소 URL: `https://github.com/42s-joowon/aiaiai`
- [ ] 개발 환경 설정 스크린샷 (VSCode, Python 버전, Git 설정)
- [ ] 프로그램 실행 결과 스크린샷 (메뉴, 추가, 목록, 검색 등)
- [ ] `git log --oneline --graph` 스크린샷

---

## 7. 학습 정리

### Git이란? 왜 필요한가?

Git은 파일의 변경 이력을 기록하는 **분산 버전 관리 시스템**입니다.

- **되돌리기:** 언제든 이전 상태로 돌아갈 수 있어 실험이 두렵지 않습니다.
- **이력 추적:** 누가, 언제, 왜 바꿨는지 커밋 메시지로 남습니다.
- **브랜치:** 기능을 독립된 줄기에서 개발하고, 완성되면 합칠 수 있습니다.
- **협업/백업:** GitHub 같은 원격 저장소에 올려 공유하고 보관합니다.

### Git 명령어

| 명령어 | 하는 일 | 이 프로젝트에서 |
|---|---|---|
| `git init` | 현재 폴더를 Git 저장소로 만든다 (`.git` 폴더 생성) | 프로젝트 시작 |
| `git add` | 변경된 파일을 다음 커밋에 담을 준비 영역(stage)에 올린다 | 기능 구현 후 `git add prompt_manager.py` |
| `git commit` | stage에 올린 변경을 메시지와 함께 하나의 기록으로 저장 | 기능 단위 커밋 (`feat: 검색 기능 구현` 등) |
| `git push` | 로컬 커밋을 원격 저장소(GitHub)에 올린다 | `git push -u origin main` |
| `git pull` | 원격 저장소의 새 커밋을 가져와 로컬에 합친다 | 다른 PC/웹에서 수정한 내용 받기 |
| `git clone` | 원격 저장소 전체(파일+이력)를 복제해 내려받는다 | 샘플 저장소 / 내 저장소 내려받기 |
| `git checkout` | 브랜치를 이동하거나 새로 만든다 (`-b`) | `git checkout -b feature/prompt-list` |
| `git merge` | 다른 브랜치의 변경을 현재 브랜치에 합친다 | `git checkout main` → `git merge feature/prompt-list` |

### 브랜치 생성과 병합 흐름

```bash
git checkout -b feature/prompt-list   # 새 브랜치 생성 + 이동
# ... 코드 작성 ...
git add prompt_manager.py
git commit -m "feat: 프롬프트 목록 보기 기능 구현"
git checkout main                     # main으로 돌아오기
git merge --no-ff feature/prompt-list # 병합 (--no-ff: 병합 기록을 그래프에 남김)
git push origin main
```

### 이 프로그램에서 쓴 Python 기초 문법

| 문법 | 사용한 곳 |
|---|---|
| 변수 / 상수 | `CATEGORIES`, `LINE`, `DATA_FILE` |
| 리스트 | `prompts` (프롬프트 전체), `CATEGORIES` |
| 딕셔너리 | 프롬프트 하나 = `{"title", "content", "category", "favorite"}` |
| 조건문 `if/elif/else` | 메뉴 선택, 번호 범위 검사, 즐겨찾기 토글 |
| 반복문 `while` | 메인 메뉴 루프, 빈 값 재입력 |
| 반복문 `for` + `enumerate` | 번호 붙여 목록 출력 |
| 리스트 컴프리헨션 | 카테고리/검색/즐겨찾기 필터링 |
| 함수 `def` / 매개변수 / 반환값 | 기능별 함수 분리, `input_prompt_index()`가 인덱스 또는 `None` 반환 |
| 문자열 메서드 | `strip()`, `lower()`, `isdigit()`, `replace()`, f-string |
| 예외 처리 `try/except` | JSON 파일 없음/형식 오류, Ctrl+C 종료 |
