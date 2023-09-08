{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "465eba29",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "과일 이름을 입력하세요: apple\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "#1조\n",
    "\n",
    "# 리스트와 튜플을 딕셔너리로 변환\n",
    "fruits = ['apple', 'banana', 'cherry']\n",
    "prices = (100, 200, 300)\n",
    "fruit_prices = dict(zip(fruits, prices))\n",
    "\n",
    "# 사용자로부터 과일 이름 입력 받기\n",
    "fruit_name = input(\"과일 이름을 입력하세요: \")\n",
    "\n",
    "# 입력받은 과일 이름을 기반으로 가격 조회 및 출력\n",
    "if fruit_name in fruit_prices:\n",
    "    print(fruit_prices[fruit_name])\n",
    "else:\n",
    "    print(\"등록되지 않은 과일입니다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b4eae595",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "시작 인덱스를 입력해주세요: 0\n",
      "끝 인덱스를 입력해주세요: 1\n",
      "슬라이싱된 리스트가 조건에 맞지 않습니다.\n"
     ]
    }
   ],
   "source": [
    "#2조\n",
    "\n",
    "numbers = [2, 6, 1, 8, 10, 5, 3]\n",
    "\n",
    "# 사용자로부터 시작 인덱스와 끝 인덱스를 입력 받음\n",
    "start_num = int(input(\"시작 인덱스를 입력해주세요: \"))\n",
    "end_num = int(input(\"끝 인덱스를 입력해주세요: \"))\n",
    "\n",
    "# start_num과 end_num 사이의 숫자들을 슬라이싱\n",
    "sliced_numbers = numbers[start_num:end_num+1]\n",
    "\n",
    "# 숫자들의 합이 짝수이고 개수가 홀수인지 검사\n",
    "if sum(sliced_numbers) % 2 == 0 and len(sliced_numbers) % 2 == 1:\n",
    "    print(\"슬라이싱된 리스트가 조건에 부합합니다.\")\n",
    "else:\n",
    "    print(\"슬라이싱된 리스트가 조건에 맞지 않습니다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "07de5591",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "매칭온 손님의 수 : 94\n",
      "[ ] 0번 손님: 소요시간 32분\n",
      "[ ] 1번 손님: 소요시간 43분\n",
      "[ ] 2번 손님: 소요시간 28분\n",
      "[ ] 3번 손님: 소요시간 50분\n",
      "[ ] 4번 손님: 소요시간 47분\n",
      "[ ] 5번 손님: 소요시간 32분\n",
      "[O] 6번 손님: 소요시간 19분\n",
      "[ ] 7번 손님: 소요시간 9분\n",
      "[ ] 8번 손님: 소요시간 34분\n",
      "[O] 9번 손님: 소요시간 10분\n",
      "[ ] 10번 손님: 소요시간 26분\n",
      "[O] 11번 손님: 소요시간 23분\n",
      "[ ] 12번 손님: 소요시간 49분\n",
      "[ ] 13번 손님: 소요시간 42분\n",
      "[O] 14번 손님: 소요시간 18분\n",
      "[ ] 15번 손님: 소요시간 50분\n",
      "[O] 16번 손님: 소요시간 10분\n",
      "[ ] 17번 손님: 소요시간 33분\n",
      "[ ] 18번 손님: 소요시간 46분\n",
      "[O] 19번 손님: 소요시간 16분\n",
      "[ ] 20번 손님: 소요시간 48분\n",
      "[O] 21번 손님: 소요시간 12분\n",
      "[ ] 22번 손님: 소요시간 30분\n",
      "[O] 23번 손님: 소요시간 18분\n",
      "[O] 24번 손님: 소요시간 10분\n",
      "[O] 25번 손님: 소요시간 10분\n",
      "[ ] 26번 손님: 소요시간 34분\n",
      "[ ] 27번 손님: 소요시간 31분\n",
      "[ ] 28번 손님: 소요시간 29분\n",
      "[O] 29번 손님: 소요시간 12분\n",
      "[ ] 30번 손님: 소요시간 41분\n",
      "[O] 31번 손님: 소요시간 20분\n",
      "[ ] 32번 손님: 소요시간 32분\n",
      "[ ] 33번 손님: 소요시간 28분\n",
      "[O] 34번 손님: 소요시간 25분\n",
      "[ ] 35번 손님: 소요시간 35분\n",
      "[ ] 36번 손님: 소요시간 48분\n",
      "[ ] 37번 손님: 소요시간 50분\n",
      "[ ] 38번 손님: 소요시간 26분\n",
      "[ ] 39번 손님: 소요시간 30분\n",
      "[O] 40번 손님: 소요시간 22분\n",
      "[ ] 41번 손님: 소요시간 38분\n",
      "[ ] 42번 손님: 소요시간 42분\n",
      "[O] 43번 손님: 소요시간 13분\n",
      "[ ] 44번 손님: 소요시간 42분\n",
      "[O] 45번 손님: 소요시간 11분\n",
      "[ ] 46번 손님: 소요시간 6분\n",
      "[O] 47번 손님: 소요시간 19분\n",
      "[ ] 48번 손님: 소요시간 35분\n",
      "[ ] 49번 손님: 소요시간 40분\n",
      "[ ] 50번 손님: 소요시간 47분\n",
      "[ ] 51번 손님: 소요시간 9분\n",
      "[O] 52번 손님: 소요시간 15분\n",
      "[ ] 53번 손님: 소요시간 8분\n",
      "[O] 54번 손님: 소요시간 12분\n",
      "[O] 55번 손님: 소요시간 22분\n",
      "[O] 56번 손님: 소요시간 23분\n",
      "[ ] 57번 손님: 소요시간 48분\n",
      "[ ] 58번 손님: 소요시간 9분\n",
      "[ ] 59번 손님: 소요시간 26분\n",
      "[O] 60번 손님: 소요시간 12분\n",
      "[ ] 61번 손님: 소요시간 31분\n",
      "[O] 62번 손님: 소요시간 19분\n",
      "[ ] 63번 손님: 소요시간 34분\n",
      "[O] 64번 손님: 소요시간 15분\n",
      "[ ] 65번 손님: 소요시간 38분\n",
      "[O] 66번 손님: 소요시간 24분\n",
      "[ ] 67번 손님: 소요시간 6분\n",
      "[ ] 68번 손님: 소요시간 38분\n",
      "[ ] 69번 손님: 소요시간 40분\n",
      "[ ] 70번 손님: 소요시간 32분\n",
      "[ ] 71번 손님: 소요시간 26분\n",
      "[ ] 72번 손님: 소요시간 6분\n",
      "[O] 73번 손님: 소요시간 15분\n",
      "[O] 74번 손님: 소요시간 16분\n",
      "[O] 75번 손님: 소요시간 20분\n",
      "[ ] 76번 손님: 소요시간 9분\n",
      "[ ] 77번 손님: 소요시간 31분\n",
      "[O] 78번 손님: 소요시간 14분\n",
      "[ ] 79번 손님: 소요시간 33분\n",
      "[ ] 80번 손님: 소요시간 9분\n",
      "[O] 81번 손님: 소요시간 11분\n",
      "[ ] 82번 손님: 소요시간 26분\n",
      "[ ] 83번 손님: 소요시간 35분\n",
      "[ ] 84번 손님: 소요시간 40분\n",
      "[ ] 85번 손님: 소요시간 38분\n",
      "[O] 86번 손님: 소요시간 12분\n",
      "[ ] 87번 손님: 소요시간 46분\n",
      "[ ] 88번 손님: 소요시간 28분\n",
      "[ ] 89번 손님: 소요시간 29분\n",
      "[O] 90번 손님: 소요시간 12분\n",
      "[ ] 91번 손님: 소요시간 43분\n",
      "[ ] 92번 손님: 소요시간 8분\n",
      "[ ] 93번 손님: 소요시간 29분\n",
      "총 탑승 인원 : 32\n",
      "총 주행 시간 : 8시간 30분\n",
      "총 수익 : 255000원\n"
     ]
    }
   ],
   "source": [
    "from random import randrange\n",
    "\n",
    "# 초기화\n",
    "total_drive_time = 0\n",
    "total_passenger_count = 0\n",
    "income = 0\n",
    "\n",
    "# 손님 매칭\n",
    "customer_count = randrange(10, 101)\n",
    "print(f\"매칭온 손님의 수 : {customer_count}\")\n",
    "\n",
    "for i in range(customer_count):\n",
    "    drive_time = randrange(5, 51)  # 승객별 운행 소요시간 (5~50분)\n",
    "    \n",
    "    # 소요시간이 10~25분 사이인지 확인\n",
    "    if 10 <= drive_time <= 25:\n",
    "        print(f\"[O] {i}번 손님: 소요시간 {drive_time}분\")\n",
    "        total_drive_time += drive_time\n",
    "        total_passenger_count += 1\n",
    "        income += drive_time * 500  # 1분당 500원\n",
    "    else:\n",
    "        print(f\"[ ] {i}번 손님: 소요시간 {drive_time}분\")\n",
    "\n",
    "# 총 주행시간 계산\n",
    "hours = total_drive_time // 60\n",
    "minutes = total_drive_time % 60\n",
    "\n",
    "# 결과 출력\n",
    "print(f\"총 탑승 인원 : {total_passenger_count}\")\n",
    "if hours > 0:\n",
    "    print(f\"총 주행 시간 : {hours}시간 {minutes}분\")\n",
    "else:\n",
    "    print(f\"총 주행 시간 : {minutes}분\")\n",
    "print(f\"총 수익 : {income}원\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c6660d91",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "    *\n",
      "   ***\n",
      "  *****\n",
      " *******\n",
      "*********\n",
      " *******\n",
      "  *****\n",
      "   ***\n",
      "    *\n"
     ]
    }
   ],
   "source": [
    "n = int(input())\n",
    "\n",
    "# 상단 부분\n",
    "for i in range(1, n + 1):\n",
    "    print(\" \" * (n - i) + \"*\" * (2 * i - 1))\n",
    "\n",
    "# 하단 부분\n",
    "for i in range(n - 1, 0, -1):\n",
    "    print(\" \" * (n - i) + \"*\" * (2 * i - 1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7c84c651",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "영어 문장을 입력하세요: apple\n",
      "자음: ppl\n",
      "모음: ae\n",
      "자음의 갯수: 3\n",
      "모음의 갯수: 2\n"
     ]
    }
   ],
   "source": [
    "sentence = input(\"영어 문장을 입력하세요: \")\n",
    "\n",
    "vowels = \"aeiouAEIOU\"\n",
    "consonants = \"bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ\"\n",
    "\n",
    "vowel_list = [char for char in sentence if char in vowels and char != \" \"]\n",
    "consonant_list = [char for char in sentence if char in consonants and char != \" \"]\n",
    "\n",
    "print(\"자음:\", ''.join(consonant_list))\n",
    "print(\"모음:\", ''.join(vowel_list))\n",
    "print(\"자음의 갯수:\", len(consonant_list))\n",
    "print(\"모음의 갯수:\", len(vowel_list))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "56606f42",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "가위/바위/보 중 선택해주세요: 바위\n",
      "컴퓨터 선택: 가위\n",
      "승리!\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "def check_winner(player, computer):\n",
    "    if player == computer:\n",
    "        return \"draw\"\n",
    "    elif (player == \"가위\" and computer == \"보\") or \\\n",
    "         (player == \"바위\" and computer == \"가위\") or \\\n",
    "         (player == \"보\" and computer == \"바위\"):\n",
    "        return \"win\"\n",
    "    else:\n",
    "        return \"lose\"\n",
    "\n",
    "while True:\n",
    "    player = input(\"가위/바위/보 중 선택해주세요: \")\n",
    "    computer = random.choice([\"가위\", \"바위\", \"보\"])\n",
    "    print(\"컴퓨터 선택:\", computer)\n",
    "    \n",
    "    result = check_winner(player, computer)\n",
    "    if result == \"win\":\n",
    "        print(\"승리!\")\n",
    "        break\n",
    "    elif result == \"lose\":\n",
    "        print(\"패배!\")\n",
    "        break\n",
    "    else:\n",
    "        print(\"무승부! 다시 시도해주세요.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e4e6d509",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "현재 키우시는 캐릭터 정보를 입력하세요\n",
      "이름 : \n",
      "str : \n",
      "luk : \n",
      "dex : \n",
      "int : \n",
      "\n",
      "이름 : 박시온\n",
      "str : 10\n",
      "luk : 1\n",
      "dex : 10\n",
      "int : 1\n",
      "\n",
      "\n",
      "이름 : 박시온\n",
      "str : 10\n",
      "luk : 1\n",
      "dex : 10\n",
      "int : 1\n"
     ]
    }
   ],
   "source": [
    "character_info = []\n",
    "\n",
    "prompt = \"\"\"\n",
    "현재 키우시는 캐릭터 정보를 입력하세요\n",
    "이름 : \n",
    "str : \n",
    "luk : \n",
    "dex : \n",
    "int : \n",
    "\"\"\"\n",
    "\n",
    "print(prompt)\n",
    "\n",
    "keys = [\"이름\", \"str\", \"luk\", \"dex\", \"int\"]\n",
    "\n",
    "for key in keys:\n",
    "    value = input(f\"{key} : \")\n",
    "    character_info.append((key, value))\n",
    "\n",
    "print(\"\\n\")\n",
    "for key, value in character_info:\n",
    "    print(f\"{key} : {value}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b380f8bd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
