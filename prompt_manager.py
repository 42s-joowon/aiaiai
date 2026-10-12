"""나만의 프롬프트 관리 프로그램 (Prompt Manager)

터미널에서 메뉴 번호를 입력해 프롬프트를 추가/조회/검색하고
즐겨찾기를 관리하는 콘솔 프로그램입니다.
데이터는 프로그램이 실행되는 동안에만 유지됩니다.
"""

# 미리 정의된 카테고리 목록
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

# 화면 구분선
LINE = "─" * 40


def create_default_prompts():
    """이전 미션에서 작성한 프롬프트를 기본 데이터로 만들어 반환한다."""
    return [
        {
            "title": "블로그 글 작성 도우미",
            "content": (
                "당신은 10년 경력의 전문 블로거입니다.\n"
                "주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요.\n"
                "서론, 본론, 결론 구조를 갖추고,\n"
                "독자의 관심을 끄는 제목을 3개 제안해주세요."
            ),
            "category": "텍스트 생성",
            "favorite": True,
        },
        {
            "title": "제품 썸네일 생성",
            "content": (
                "다음 제품의 매력적인 썸네일 이미지를 생성해주세요.\n"
                "제품: [제품명]\n"
                "스타일: 미니멀, 파스텔 톤 배경, 부드러운 자연광, 정면 45도 구도\n"
                "비율: 1:1, 고해상도, 텍스트 없음"
            ),
            "category": "이미지 생성",
            "favorite": False,
        },
        {
            "title": "IT 컨설턴트 페르소나",
            "content": (
                "너는 15년 차 IT 컨설턴트 '김정확'이야.\n"
                "비전공자도 이해할 수 있도록 비유를 들어 설명하고,\n"
                "항상 '현황 → 문제점 → 해결책' 순서로 답변해.\n"
                "모르는 내용은 추측하지 말고 모른다고 말해."
            ),
            "category": "페르소나",
            "favorite": False,
        },
        {
            "title": "뉴스 요약 프롬프트",
            "content": (
                "아래 뉴스 기사를 읽고 다음 형식으로 요약해줘.\n"
                "1) 한 줄 요약\n"
                "2) 핵심 내용 3가지 (불릿)\n"
                "3) 관련 키워드 5개\n"
                "결과는 슬랙 메시지로 바로 보낼 수 있게 마크다운으로 작성해줘."
            ),
            "category": "자동화",
            "favorite": False,
        },
        {
            "title": "광고 스크립트 작성",
            "content": (
                "15초 분량의 숏폼 광고 영상 스크립트를 작성해줘.\n"
                "제품: [제품명], 타깃: 20대 직장인\n"
                "장면(Scene)별로 화면 묘사, 자막, 내레이션을 표로 정리하고\n"
                "첫 3초 안에 시선을 끄는 훅(Hook)을 넣어줘."
            ),
            "category": "영상 생성",
            "favorite": False,
        },
    ]


# ──────────────────────────────────────────
# 입력 도우미 함수
# ──────────────────────────────────────────

def input_required(label):
    """빈 값이 아닌 입력을 받을 때까지 반복해서 묻는다."""
    while True:
        value = input(label).strip()
        if value:
            return value
        print("값이 비어 있습니다. 다시 입력해주세요.")


def get_categories(prompts):
    """기본 카테고리 + 사용자가 직접 입력한 카테고리 목록을 반환한다."""
    categories = list(CATEGORIES)
    for prompt in prompts:
        if prompt["category"] not in categories:
            categories.append(prompt["category"])
    return categories


def print_categories(categories):
    """카테고리 목록을 번호와 함께 출력한다."""
    for index, category in enumerate(categories, start=1):
        print(f"{index}) {category}")


def select_category(prompts):
    """카테고리를 번호로 선택하거나 직접 입력받아 반환한다."""
    categories = get_categories(prompts)
    custom_number = len(categories) + 1

    print("\n카테고리 선택:")
    print_categories(categories)
    print(f"{custom_number}) 직접 입력")

    while True:
        choice = input_required("선택: ")
        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            return categories[int(choice) - 1]
        if choice == str(custom_number):
            return input_required("새 카테고리 이름: ")
        print(f"1~{custom_number} 사이의 번호를 입력해주세요.")


# ──────────────────────────────────────────
# 기능 함수
# ──────────────────────────────────────────

def add_prompt(prompts):
    """새 프롬프트를 입력받아 목록에 추가한다."""
    print("=== 프롬프트 추가 ===")
    title = input_required("제목: ")
    content = input_required("내용: ")
    category = select_category(prompts)

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
    })
    print("\n프롬프트가 추가되었습니다!")


def format_prompt_line(number, prompt):
    """목록 한 줄 형식: '번호. [카테고리] 제목 ⭐'"""
    star = " ⭐" if prompt["favorite"] else ""
    return f"{number}. [{prompt['category']}] {prompt['title']}{star}"


def print_prompt_lines(numbered_prompts):
    """(번호, 프롬프트) 목록을 한 줄씩 출력한다."""
    for number, prompt in numbered_prompts:
        print(format_prompt_line(number, prompt))


def numbered(prompts):
    """프롬프트마다 전체 목록 기준 번호(1부터)를 붙여 반환한다."""
    return list(enumerate(prompts, start=1))


def show_list(prompts):
    """저장된 모든 프롬프트를 번호와 함께 출력한다."""
    print("=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다. 먼저 프롬프트를 추가해주세요.")
        return

    print_prompt_lines(numbered(prompts))
    print(f"\n총 {len(prompts)}개의 프롬프트")


# ──────────────────────────────────────────
# 메뉴 / 메인
# ──────────────────────────────────────────

def show_menu(menu_items):
    """메인 메뉴를 출력한다."""
    print()
    print("=== 나만의 프롬프트 관리 ===")
    for number, label, _ in menu_items:
        print(f"{number}. {label}")
    print("0. 종료")


def get_menu_items():
    """(번호, 메뉴 이름, 실행할 함수) 목록을 반환한다."""
    return [
        ("1", "프롬프트 추가", add_prompt),
        ("2", "프롬프트 목록", show_list),
    ]


def main():
    """프로그램 진입점: 메뉴를 보여주고 선택한 기능을 실행한다."""
    prompts = create_default_prompts()
    menu_items = get_menu_items()
    actions = {number: action for number, _, action in menu_items}

    while True:
        show_menu(menu_items)
        choice = input("선택: ").strip()

        if choice == "0":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break

        action = actions.get(choice)
        if action is None:
            print(f"잘못된 입력입니다. 0~{len(menu_items)} 사이의 번호를 입력해주세요.")
            continue

        print()
        action(prompts)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n프로그램을 종료합니다.")
