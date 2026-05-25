TOPUP_FAQ = {
    "mobile legends": "Untuk top up Mobile Legends, beli Diamond via menu Top Up di dalam game atau melalui platform resmi.",
    "free fire": "Untuk top up Free Fire, beli Diamond via menu Top Up di dalam game atau melalui Garena official.",
    "valorant": "Untuk top up Valorant, beli VP (Valorant Points) via Riot Games official website.",
    "genshin": "Untuk top up Genshin Impact, beli Genesis Crystal via menu Top Up di dalam game.",
}

def get_answer(question: str) -> str:
    question_lower = question.lower()
    for keyword, answer in TOPUP_FAQ.items():
        if keyword in question_lower:
            return answer
    return "Maaf, saya belum punya informasi untuk pertanyaan itu. Silakan hubungi CS kami."