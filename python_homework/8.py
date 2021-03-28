def check_and_clear(box):
    print("불량품이 있으면 box를 clear합니다.")
    if "불량품" in box.keys() :
        box.clear()
box1 = {"불량품" : 10}
check_and_clear(box1)

print(box1)

box2 = {"정상품": 10}
check_and_clear(box2)

print(box2)