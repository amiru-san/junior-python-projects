print("=== USERNAME RATER ===")

print(f"\nWARNING: This algorithm merely predicts the score based on username basic conditions.\nThe algorithm does not rely on username trends or popularity.\n")

nocaut = [
    "(+) No numbers included",
    "(+) No underscore included.",
    "(+) Short (4-5 characters).",
    "(+) No double letters."
]

caut = [
    "(-) Contains numbers.",
    "(-) Contains underscore.",
    "Too short!",
    "No spaces in the input!",
    "It cannot be only with numbers!",
    "There must be only letters and numbers!",
    "(-) Long.",
    "(-) Double letter/number."
]

prohibited = "@#$&-+()/*':;!?~`|•√π÷×§∆£¢€¥^°={}%©®™✓[]¹²³⁴⁵⁶⁷⁸⁹⁰½⅓¼⅕⅙⅐⅛⅑⅒⅔⅖⅗¾⅜⅘⅝⅚⅞ⁿ∅№₹¥₱€¢£—–·±<>★†‡„“”«»‚‘’‹›¡¿‽♪ΩΠμ¶←↑↓→∞≠≈‰℅"

nums = "1234567890"

while True:
    count = 0
    
    user= input("Username: ").strip()

    if user.isdigit():
        print(caut[4])
        continue
    elif any(" " in user for c in user):
        print(caut[3])
        continue
    elif any(c in prohibited for c in user):
        print(caut[5])
        continue
    elif len(user) < 4:
        print(caut[2])
        continue
    # start
    print(f"\n===============\n{user}\n===============\n\nOverall:\n")
    if any(c in nums for c in user):
        print(caut[0])
    else:
        count += 2
        print(nocaut[0])
    if any("_" in user for c in user):
        print(caut[1])
    else:
        count += 2
        print(nocaut[1])
    if len(user) > 5:
        count += 1
        print(caut[6])
    elif len(user) > 6:
        print(caut[6])
    else:
        count += 2
        print(nocaut[2])
    if any(user[i] == user[i+1] for i in range(len(user) - 1)):
        print(caut[7])
    else:
        count += 1
        print(nocaut[3])
    
    if count == 1:
        print(f"\nStatus: VERY LOW\n★–––––– 1 / 7\n")
    elif count == 2:
        print(f"\nStatus: LOW\n★★––––– 2 / 7\n")
    elif count == 3:
        print(f"\nStatus: MEDIUM\n★★★–––– 3 / 7\n")
    elif count == 4:
        print(f"\nStatus: NORMAL\n★★★★––– 4 / 7\n")
    elif count == 5:
        print(f"\nStatus: HIGH\n★★★★★–– 5 / 7\n")
    elif count == 6:
        print(f"\nStatus: VERY HIGH\n★★★★★★– 6 / 7\n")
    elif count == 7:
        print(f"\nStatus: GREAT\n★★★★★★★ 7 / 7\n")
    else:
        print(f"\nStatus: IMPOSSIBLE\n–––––– 0 / 6\n")