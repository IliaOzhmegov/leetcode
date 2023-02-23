from LC_716_Max_Stack import MaxStack

if __name__ == '__main__':
    ms = MaxStack()

    assert None == ms.push(85)
    assert None == ms.push(-34)
    assert None == ms.push(17)
    assert 85 == ms.popMax()
    assert 17 == ms.top()
    assert None == ms.push(10)
    assert None == ms.push(-37)
    assert None == ms.push(93)
    assert 93 == ms.peekMax()
    assert None == ms.push(-86)
    assert -86 == ms.top()
    assert 93 == ms.popMax()
    assert 17 == ms.peekMax()
    assert -86 == ms.pop()
    assert None == ms.push(4)
    assert None == ms.push(15)
    assert None == ms.push(82)
    assert 82 == ms.peekMax()
    assert 82 == ms.pop()
    assert 17 == ms.peekMax()
    assert None == ms.push(54)
    assert None == ms.push(-19)
    assert -19 == ms.pop()
    assert 54 == ms.pop()
    assert None == ms.push(-5)
    assert 17 == ms.popMax()
    assert 15 == ms.popMax()
    assert None == ms.push(83)
    assert 83 == ms.top()
    assert None == ms.push(81)
    assert 83 == ms.peekMax()
    assert None == ms.push(65)
    assert 65 == ms.top()
    assert 83 == ms.popMax()
    assert 81 == ms.peekMax()
    assert 65 == ms.top()
    assert None == ms.push(-46)
    assert None == ms.push(91)
    assert 91 == ms.top()
    assert None == ms.push(94)
    assert None == ms.push(-18)
    assert None == ms.push(-30)
    assert 94 == ms.peekMax()
    assert -30 == ms.top()
    assert None == ms.push(74)
    assert None == ms.push(69)
    assert 69 == ms.pop()
    assert 74 == ms.pop()
    assert None == ms.push(13)
    assert 94 == ms.popMax()
    assert 13 == ms.pop()
    assert -30 == ms.top()
    assert -30 == ms.top()
    assert None == ms.push(85)
    assert None == ms.push(-72)
    assert 91 == ms.popMax()
    assert -72 == ms.top()
    assert 85 == ms.peekMax()
    assert None == ms.push(-58)
    assert None == ms.push(68)
    assert 68 == ms.pop()
    assert -58 == ms.top()
    assert 85 == ms.popMax()
    assert None == ms.push(51)
    assert None == ms.push(-68)
    assert -68 == ms.top()
    assert None == ms.push(9)
    assert None == ms.push(94)
    assert 94 == ms.top()
    assert 94 == ms.top()
    assert 94 == ms.popMax()
    assert None == ms.push(56)
    assert None == ms.push(-29)
    assert None == ms.push(90)
    assert 90 == ms.top()
    assert 90 == ms.top()
    assert None == ms.push(-94)
    assert None == ms.push(-6)
    assert 90 == ms.peekMax()
    assert None == ms.push(-62)
    assert -62 == ms.top()
    assert 90 == ms.popMax()
    assert None == ms.push(-9)
    assert 81 == ms.peekMax()
    assert None == ms.push(-76)
    assert 81 == ms.peekMax()
    assert 81 == ms.popMax()
    assert -76 == ms.pop()
    assert None == ms.push(8)
    assert 8 == ms.top()
    assert 65 == ms.peekMax()
    assert None == ms.push(-45)
    assert 65 == ms.popMax()
    assert None == ms.push(-6)
    assert None == ms.push(-100)
    assert None == ms.push(56)
    assert 56 == ms.pop()
    assert None == ms.push(-33)
    assert -33 == ms.pop()
    assert None == ms.push(-86)
    assert -86 == ms.pop()
    assert None == ms.push(20)
    assert 56 == ms.peekMax()
    assert None == ms.push(20)
    assert None == ms.push(2)
    assert None == ms.push(-35)
    assert None == ms.push(-82)
    assert None == ms.push(67)
    assert 67 == ms.top()
    assert None == ms.push(-34)
    assert 67 == ms.peekMax()
    assert None == ms.push(45)
    assert 45 == ms.pop()
    assert None == ms.push(25)
    assert 67 == ms.peekMax()
    assert 67 == ms.popMax()
    assert 56 == ms.popMax()
    assert 51 == ms.peekMax()
    assert 25 == ms.top()
    assert 25 == ms.pop()
    assert 51 == ms.peekMax()
    assert -34 == ms.pop()
    assert None == ms.push(-5)
    assert None == ms.push(-24)
    assert None == ms.push(-89)
    assert None == ms.push(26)
    assert 51 == ms.popMax()
    assert None == ms.push(94)
    assert None == ms.push(-43)
    assert -43 == ms.top()
    assert None == ms.push(-64)
    assert None == ms.push(-41)
    assert None == ms.push(-43)
    assert None == ms.push(-42)
    assert 94 == ms.popMax()
    assert -42 == ms.pop()
    assert 26 == ms.peekMax()
    assert None == ms.push(20)
    assert 26 == ms.peekMax()
    assert 26 == ms.popMax()
    assert 20 == ms.popMax()
    assert 20 == ms.peekMax()
    assert None == ms.push(29)
    assert None == ms.push(-63)
    assert None == ms.push(100)
    assert 100 == ms.popMax()
    assert None == ms.push(88)
    assert 88 == ms.peekMax()
    assert 88 == ms.pop()
    assert None == ms.push(-70)
    assert 29 == ms.popMax()
    assert None == ms.push(-78)
    assert -78 == ms.top()
    assert 20 == ms.peekMax()
    assert 20 == ms.peekMax()
    assert 20 == ms.popMax()
    assert 20 == ms.popMax()
    assert -78 == ms.top()
    assert -78 == ms.top()
    assert -78 == ms.top()
    assert 10 == ms.peekMax()
    assert 10 == ms.peekMax()
    assert None == ms.push(98)
    assert 98 == ms.top()
    assert None == ms.push(10)
    assert 10 == ms.top()
    assert 98 == ms.peekMax()
    assert 10 == ms.pop()
    assert 98 == ms.popMax()
    assert None == ms.push(33)
    assert None == ms.push(-49)
    assert -49 == ms.pop()
    assert None == ms.push(51)
    assert 51 == ms.pop()
    assert None == ms.push(26)
    assert 26 == ms.pop()
    assert None == ms.push(64)
    assert 64 == ms.pop()
    assert None == ms.push(-13)
    assert 33 == ms.popMax()
    assert -13 == ms.pop()
    assert 10 == ms.peekMax()
    assert -78 == ms.pop()
    assert -70 == ms.top()
    assert -70 == ms.top()
    assert -70 == ms.pop()
    assert None == ms.push(-49)
    assert None == ms.push(-65)
    assert 10 == ms.peekMax()
    assert -65 == ms.pop()
    assert 10 == ms.peekMax()
    assert -49 == ms.top()
    assert -49 == ms.top()
    assert None == ms.push(-14)
    assert 10 == ms.popMax()
    assert None == ms.push(-98)
    assert None == ms.push(27)
    assert None == ms.push(-17)
    assert None == ms.push(-19)
    assert -19 == ms.top()
    assert None == ms.push(-98)
    assert None == ms.push(76)
    assert 76 == ms.peekMax()
    assert 76 == ms.peekMax()
    assert 76 == ms.popMax()
    assert -98 == ms.top()
    assert None == ms.push(-24)
    assert None == ms.push(-100)
    assert 27 == ms.peekMax()
    assert -100 == ms.pop()
    assert None == ms.push(-99)
    assert 27 == ms.peekMax()
    assert None == ms.push(-49)
    assert -49 == ms.top()
    assert None == ms.push(-40)
    assert None == ms.push(-95)
    assert None == ms.push(-54)
    assert None == ms.push(-50)
    assert -50 == ms.pop()
    assert None == ms.push(55)
    assert 55 == ms.pop()
    assert None == ms.push(58)
    assert None == ms.push(78)
    assert 78 == ms.pop()
    assert None == ms.push(6)
    assert 6 == ms.pop()
    assert None == ms.push(65)
    assert 65 == ms.pop()
    assert 58 == ms.pop()
    assert None == ms.push(-26)
    assert -26 == ms.top()
    assert 27 == ms.popMax()
    assert None == ms.push(59)
    assert None == ms.push(-44)
    assert 59 == ms.peekMax()
    assert 59 == ms.popMax()
    assert None == ms.push(-90)
    assert -90 == ms.top()
    assert -90 == ms.pop()
    assert -44 == ms.top()
    assert -44 == ms.top()
    assert None == ms.push(24)
    assert None == ms.push(3)
    assert 3 == ms.top()
    assert 24 == ms.peekMax()
    assert 24 == ms.popMax()
    assert 3 == ms.top()
    assert 3 == ms.pop()
    assert 9 == ms.peekMax()
    assert None == ms.push(-38)
    assert None == ms.push(-4)
    assert 9 == ms.peekMax()
    assert -4 == ms.pop()
    assert 9 == ms.popMax()
    assert None == ms.push(-63)
    assert None == ms.push(64)
    assert 64 == ms.pop()
    assert 8 == ms.peekMax()
    assert None == ms.push(1)
    assert 8 == ms.popMax()
    assert 4 == ms.popMax()
    assert None == ms.push(-59)
    assert 2 == ms.popMax()
    assert 1 == ms.peekMax()
    assert 1 == ms.peekMax()
    assert None == ms.push(89)
    assert None == ms.push(-68)
    assert -68 == ms.top()
    assert None == ms.push(-72)
    assert None == ms.push(8)
    assert None == ms.push(-41)
    assert None == ms.push(75)
    assert None == ms.push(24)
    assert None == ms.push(48)
    assert 48 == ms.pop()
    assert 24 == ms.top()
    assert None == ms.push(-27)
    assert -27 == ms.pop()
    assert None == ms.push(11)
    assert 11 == ms.pop()
    assert None == ms.push(88)
    assert 89 == ms.peekMax()
    assert 88 == ms.pop()
    assert None == ms.push(-15)
    assert None == ms.push(70)
    assert None == ms.push(-53)
    assert 89 == ms.popMax()
    assert None == ms.push(-58)
    assert None == ms.push(54)
    assert 54 == ms.pop()
    assert None == ms.push(-82)
    assert -82 == ms.pop()
    assert 75 == ms.peekMax()
    assert None == ms.push(-28)
    assert None == ms.push(-100)
    assert -100 == ms.top()
    assert 75 == ms.peekMax()
    assert -100 == ms.pop()
    assert None == ms.push(68)
    assert 68 == ms.top()
    assert None == ms.push(53)
    assert None == ms.push(-39)
    assert None == ms.push(-44)
    assert None == ms.push(-44)
    assert -44 == ms.top()
    assert None == ms.push(24)
    assert 75 == ms.peekMax()
    assert 24 == ms.top()
    assert 75 == ms.peekMax()
    assert None == ms.push(-30)
    assert None == ms.push(63)
    assert 63 == ms.top()
    assert 75 == ms.popMax()
    assert None == ms.push(-54)
    assert -54 == ms.top()
    assert -54 == ms.top()
    assert None == ms.push(21)
    assert None == ms.push(-17)
    assert 70 == ms.peekMax()
    assert 70 == ms.popMax()
    assert -17 == ms.top()
    assert -17 == ms.pop()
    assert 21 == ms.top()
    assert 21 == ms.top()
    assert 68 == ms.peekMax()
    assert 21 == ms.pop()
    assert -54 == ms.top()
    assert None == ms.push(-20)
    assert 68 == ms.popMax()
    assert -20 == ms.pop()
    assert 63 == ms.popMax()
    assert None == ms.push(-19)
    assert None == ms.push(-10)
    assert None == ms.push(56)
    assert 56 == ms.top()
    assert 56 == ms.peekMax()
    assert 56 == ms.top()
    assert 56 == ms.peekMax()
    assert 56 == ms.pop()
    assert 53 == ms.popMax()
    assert -10 == ms.top()
    assert 24 == ms.peekMax()
    assert 24 == ms.popMax()
    assert None == ms.push(2)
    assert 2 == ms.pop()
    assert None == ms.push(-69)
    assert 24 == ms.popMax()
    assert None == ms.push(-61)
    assert None == ms.push(-25)
    assert -25 == ms.pop()
    assert None == ms.push(99)
    assert 99 == ms.peekMax()
    assert 99 == ms.peekMax()
    assert 99 == ms.top()
    assert None == ms.push(51)
    assert 51 == ms.pop()
    assert 99 == ms.pop()
    assert -61 == ms.pop()
    assert -69 == ms.pop()
    assert 8 == ms.popMax()
    assert -10 == ms.top()
    assert None == ms.push(-11)
    assert 1 == ms.popMax()
    assert -5 == ms.peekMax()
    assert -5 == ms.peekMax()
    assert -11 == ms.top()
    assert None == ms.push(69)
    assert 69 == ms.top()
    assert None == ms.push(-76)
    assert None == ms.push(33)
    assert None == ms.push(-83)
    assert 69 == ms.popMax()
    assert 33 == ms.peekMax()
    assert None == ms.push(-77)
    assert -77 == ms.top()
    assert 33 == ms.peekMax()
    assert -77 == ms.top()
    assert 33 == ms.peekMax()
    assert -77 == ms.top()
    assert -77 == ms.top()
    assert 33 == ms.peekMax()
    assert None == ms.push(-49)
    assert -49 == ms.pop()
    assert None == ms.push(-61)
    assert None == ms.push(-38)
    assert None == ms.push(-69)
    assert -69 == ms.pop()
    assert None == ms.push(29)
    assert None == ms.push(-77)
    assert -77 == ms.pop()
    assert None == ms.push(-88)
    assert None == ms.push(-8)
    assert 33 == ms.popMax()
    assert None == ms.push(-21)
    assert -21 == ms.pop()
    assert -8 == ms.top()
    assert -8 == ms.pop()
    assert -88 == ms.pop()
    assert None == ms.push(2)
    assert None == ms.push(-1)
    assert -1 == ms.pop()
    assert None == ms.push(-49)
    assert None == ms.push(-84)
    assert -84 == ms.pop()
    assert 29 == ms.peekMax()
    assert None == ms.push(-86)
    assert None == ms.push(73)
    assert None == ms.push(-99)
    assert None == ms.push(-82)
    assert 73 == ms.popMax()
    assert 29 == ms.popMax()
    assert -82 == ms.pop()
    assert 2 == ms.popMax()
    assert None == ms.push(-79)
    assert None == ms.push(23)
    assert 23 == ms.top()
    assert 23 == ms.popMax()
    assert -5 == ms.peekMax()
    assert None == ms.push(21)
    assert None == ms.push(-40)
    assert 21 == ms.popMax()
    assert -40 == ms.top()
    assert None == ms.push(-22)
    assert None == ms.push(36)
    assert None == ms.push(56)
    assert 56 == ms.pop()
    assert None == ms.push(-85)
    assert None == ms.push(29)
    assert None == ms.push(91)
    assert 91 == ms.peekMax()
    assert None == ms.push(-28)
    assert 91 == ms.peekMax()
    assert 91 == ms.popMax()
    assert 36 == ms.peekMax()
    assert -28 == ms.pop()
    assert None == ms.push(89)
    assert 89 == ms.pop()
    assert None == ms.push(14)
    assert 36 == ms.popMax()
    assert 29 == ms.peekMax()
    assert None == ms.push(78)
    assert None == ms.push(8)
    assert None == ms.push(84)
    assert None == ms.push(-82)
    assert 84 == ms.popMax()
    assert None == ms.push(-83)
    assert 78 == ms.peekMax()
    assert None == ms.push(-46)
    assert None == ms.push(-64)
    assert -64 == ms.pop()
    assert -46 == ms.pop()
    assert -83 == ms.pop()
    assert None == ms.push(-63)
    assert None == ms.push(84)
    assert 84 == ms.peekMax()
    assert 84 == ms.peekMax()
    assert 84 == ms.peekMax()
    assert 84 == ms.pop()
    assert -63 == ms.top()
    assert None == ms.push(32)
    assert 32 == ms.pop()
    assert None == ms.push(-17)
    assert -17 == ms.pop()
    assert None == ms.push(-4)
    assert 78 == ms.popMax()
    assert 29 == ms.peekMax()
    assert 29 == ms.peekMax()
    assert None == ms.push(-57)
    assert -57 == ms.top()
    assert None == ms.push(78)
    assert None == ms.push(-100)
    assert 78 == ms.popMax()
    assert 29 == ms.peekMax()
    assert -100 == ms.top()
    assert None == ms.push(-30)
    assert 29 == ms.popMax()
    assert -30 == ms.pop()
    assert 14 == ms.peekMax()
    assert None == ms.push(64)
    assert None == ms.push(90)
    assert 90 == ms.top()
    assert None == ms.push(51)
    assert 51 == ms.top()
    assert 90 == ms.peekMax()
    assert 51 == ms.pop()
    assert 90 == ms.top()
    assert 90 == ms.peekMax()
    assert 90 == ms.top()
    assert 90 == ms.popMax()
    assert 64 == ms.popMax()
    assert -100 == ms.pop()
    assert None == ms.push(-38)
    assert 14 == ms.popMax()
    assert -38 == ms.pop()
    assert -57 == ms.pop()
    assert None == ms.push(-84)
    assert None == ms.push(-72)
    assert 8 == ms.popMax()
    assert -72 == ms.top()
    assert None == ms.push(-13)
    assert None == ms.push(-15)
    assert -4 == ms.peekMax()
    assert -15 == ms.top()
    assert None == ms.push(45)
    assert 45 == ms.top()
    assert None == ms.push(81)
    assert 81 == ms.peekMax()
    assert 81 == ms.top()
    assert 81 == ms.top()
    assert None == ms.push(63)
    assert 81 == ms.popMax()
    assert None == ms.push(70)
    assert 70 == ms.popMax()
    assert None == ms.push(27)
    assert None == ms.push(67)
    assert 67 == ms.top()
    assert 67 == ms.peekMax()
    assert None == ms.push(-81)
    assert -81 == ms.top()
    assert -81 == ms.top()
    assert None == ms.push(-38)
    assert None == ms.push(41)
    assert None == ms.push(-23)
    assert None == ms.push(-37)
    assert None == ms.push(-77)
    assert 67 == ms.peekMax()
    assert None == ms.push(2)
    assert None == ms.push(52)
    assert 67 == ms.popMax()
    assert 63 == ms.popMax()
    assert None == ms.push(-30)
    assert -30 == ms.pop()
    assert None == ms.push(9)
    assert 9 == ms.top()
    assert 52 == ms.popMax()
    assert 9 == ms.pop()
    assert 45 == ms.popMax()
    assert 2 == ms.pop()
    assert 41 == ms.popMax()
    assert 27 == ms.popMax()
    assert -77 == ms.pop()
    assert -4 == ms.popMax()
    assert -37 == ms.top()
    assert -5 == ms.popMax()
    assert -37 == ms.top()
    assert -5 == ms.peekMax()
    assert None == ms.push(2)
    assert 2 == ms.pop()
    assert -5 == ms.peekMax()
    assert None == ms.push(-78)
    assert -78 == ms.top()
    assert -78 == ms.top()
    assert -78 == ms.top()
    assert None == ms.push(18)
    assert 18 == ms.popMax()
    assert None == ms.push(37)
    assert 37 == ms.peekMax()
    assert None == ms.push(-53)
    assert 37 == ms.peekMax()
    assert None == ms.push(-2)
    assert -2 == ms.pop()
    assert None == ms.push(-67)
    assert -67 == ms.top()
    assert 37 == ms.peekMax()
    assert 37 == ms.peekMax()
    assert 37 == ms.popMax()
    assert -67 == ms.pop()
    assert -5 == ms.popMax()
    assert None == ms.push(6)
    assert None == ms.push(64)
    assert 64 == ms.popMax()
    assert None == ms.push(63)
    assert 63 == ms.peekMax()
    assert None == ms.push(-67)
    assert -67 == ms.top()
    assert None == ms.push(0)
    assert 0 == ms.top()
    assert 0 == ms.top()
    assert 63 == ms.popMax()
    assert 6 == ms.peekMax()
    assert 0 == ms.pop()
    assert 6 == ms.popMax()
    assert -6 == ms.peekMax()
    assert -67 == ms.pop()
    assert None == ms.push(-48)
    assert None == ms.push(0)
    assert None == ms.push(-19)
    assert 0 == ms.peekMax()
    assert -19 == ms.top()
    assert None == ms.push(78)
    assert 78 == ms.peekMax()
    assert None == ms.push(-79)
    assert -79 == ms.pop()
    assert 78 == ms.peekMax()
    assert 78 == ms.top()
    assert 78 == ms.pop()
    assert None == ms.push(11)
    assert 11 == ms.peekMax()
    assert 11 == ms.popMax()
    assert None == ms.push(-74)
    assert -74 == ms.top()
    assert None == ms.push(-11)
    assert None == ms.push(16)
    assert 16 == ms.popMax()
    assert 0 == ms.popMax()
    assert None == ms.push(70)
    assert 70 == ms.popMax()
    assert None == ms.push(32)
    assert None == ms.push(-97)
    assert 32 == ms.popMax()
    assert None == ms.push(16)
    assert 16 == ms.top()
    assert None == ms.push(-64)
    assert None == ms.push(2)
    assert None == ms.push(-72)
    assert -72 == ms.top()
    assert -72 == ms.top()
    assert 16 == ms.peekMax()
    assert -72 == ms.pop()
    assert 2 == ms.pop()
    assert None == ms.push(-55)
    assert 16 == ms.peekMax()
    assert None == ms.push(50)
    assert 50 == ms.peekMax()
    assert None == ms.push(-2)
    assert None == ms.push(-71)
    assert 50 == ms.popMax()
    assert None == ms.push(23)
    assert None == ms.push(100)
    assert 100 == ms.popMax()
    assert 23 == ms.peekMax()
    assert 23 == ms.popMax()
    assert None == ms.push(-54)
    assert None == ms.push(-48)
    assert 16 == ms.popMax()
    assert None == ms.push(-40)
    assert None == ms.push(-70)
    assert -2 == ms.popMax()
    assert -6 == ms.peekMax()
    assert None == ms.push(55)
    assert 55 == ms.peekMax()
    assert 55 == ms.popMax()
    assert None == ms.push(99)
    assert 99 == ms.popMax()
    assert None == ms.push(-32)
    assert -32 == ms.top()
    assert -6 == ms.peekMax()
    assert None == ms.push(48)
    assert None == ms.push(-19)
    assert -19 == ms.pop()
    assert None == ms.push(74)
    assert 74 == ms.popMax()
    assert None == ms.push(79)
    assert None == ms.push(-24)
    assert -24 == ms.pop()
    assert None == ms.push(-33)
    assert None == ms.push(-12)
    assert None == ms.push(-25)
    assert None == ms.push(-63)
    assert -63 == ms.top()
    assert None == ms.push(69)
    assert 69 == ms.top()
    assert 69 == ms.pop()
    assert -63 == ms.top()
    assert None == ms.push(-99)
    assert -99 == ms.pop()
    assert None == ms.push(8)
    assert None == ms.push(96)
    assert 96 == ms.top()
    assert 96 == ms.top()
    assert 96 == ms.peekMax()
    assert 96 == ms.pop()
    assert None == ms.push(21)
    assert 79 == ms.popMax()
    assert 48 == ms.peekMax()
    assert 21 == ms.top()
    assert 48 == ms.popMax()
    assert None == ms.push(67)
    assert 67 == ms.popMax()
    assert 21 == ms.top()
    assert 21 == ms.peekMax()
    assert 21 == ms.popMax()
    assert None == ms.push(64)
    assert 64 == ms.peekMax()
    assert None == ms.push(-58)
    assert -58 == ms.pop()
    assert 64 == ms.popMax()
    assert None == ms.push(-9)
    assert -9 == ms.top()
    assert 8 == ms.popMax()
    assert -9 == ms.top()
    assert -9 == ms.pop()
    assert -63 == ms.top()
    assert None == ms.push(53)
    assert None == ms.push(-54)
    assert 53 == ms.peekMax()
    assert 53 == ms.popMax()
    assert -54 == ms.top()
    assert None == ms.push(57)
    assert 57 == ms.peekMax()
    assert 57 == ms.popMax()
    assert None == ms.push(10)
    assert 10 == ms.pop()
    assert -6 == ms.popMax()
    assert None == ms.push(41)
    assert None == ms.push(-99)
    assert 41 == ms.popMax()
    assert None == ms.push(-5)
    assert None == ms.push(74)
    assert 74 == ms.top()
    assert None == ms.push(-29)
    assert 74 == ms.peekMax()
    assert None == ms.push(-89)
    assert -89 == ms.pop()
    assert None == ms.push(89)
    assert None == ms.push(80)
    assert 80 == ms.top()
    assert 89 == ms.peekMax()
    assert 89 == ms.peekMax()
    assert 89 == ms.popMax()
    assert 80 == ms.pop()
    assert None == ms.push(-60)
    assert None == ms.push(-62)
    assert -62 == ms.pop()
    assert None == ms.push(-77)
    assert 74 == ms.peekMax()
    assert None == ms.push(-71)
    assert None == ms.push(14)
    assert None == ms.push(-11)
    assert None == ms.push(36)
    assert None == ms.push(90)
    assert None == ms.push(-19)
    assert -19 == ms.pop()
    assert None == ms.push(86)
    assert 90 == ms.popMax()
    assert 86 == ms.popMax()
    assert None == ms.push(-43)
    assert None == ms.push(39)
    assert None == ms.push(85)
    assert None == ms.push(66)
    assert 85 == ms.peekMax()
    assert 66 == ms.pop()
    assert None == ms.push(89)
    assert 89 == ms.peekMax()
    assert None == ms.push(9)
    assert None == ms.push(-19)
    assert None == ms.push(36)
    assert None == ms.push(-89)
    assert -89 == ms.top()
    assert -89 == ms.pop()
    assert 89 == ms.peekMax()
    assert 36 == ms.top()
    assert 89 == ms.peekMax()
    assert 36 == ms.top()
    assert None == ms.push(-47)
    assert 89 == ms.popMax()
    assert 85 == ms.peekMax()
    assert None == ms.push(62)
    assert 62 == ms.pop()
    assert 85 == ms.peekMax()
    assert None == ms.push(-36)
    assert -36 == ms.pop()
    assert None == ms.push(72)
    assert 85 == ms.popMax()
    assert None == ms.push(39)
    assert 74 == ms.popMax()
    assert None == ms.push(-61)
    assert 72 == ms.peekMax()
    assert 72 == ms.popMax()
    assert -61 == ms.top()
    assert None == ms.push(47)
    assert None == ms.push(-40)
    assert -40 == ms.top()
    assert None == ms.push(-76)
    assert None == ms.push(73)
    assert None == ms.push(-42)
    assert None == ms.push(59)
    assert 73 == ms.peekMax()
    assert None == ms.push(19)
    assert None == ms.push(94)
    assert None == ms.push(-24)
    assert 94 == ms.peekMax()
    assert -24 == ms.top()
    assert 94 == ms.peekMax()
    assert 94 == ms.peekMax()
    assert None == ms.push(47)
    assert None == ms.push(-72)
    assert -72 == ms.pop()
    assert 94 == ms.popMax()
    assert 73 == ms.popMax()
    assert None == ms.push(63)
    assert None == ms.push(42)
    assert None == ms.push(-45)
    assert None == ms.push(54)
    assert None == ms.push(19)
    assert None == ms.push(-41)
    assert 63 == ms.popMax()
    assert 59 == ms.peekMax()
    assert -41 == ms.pop()
    assert 59 == ms.popMax()
    assert 54 == ms.peekMax()
    assert 54 == ms.peekMax()
    assert 54 == ms.popMax()
    assert None == ms.push(9)
    assert 47 == ms.peekMax()
    assert 47 == ms.peekMax()
    assert 9 == ms.top()
    assert 9 == ms.pop()
    assert 47 == ms.peekMax()
    assert 19 == ms.pop()
    assert 47 == ms.peekMax()
    assert 47 == ms.popMax()
    assert 47 == ms.peekMax()
    assert None == ms.push(60)
    assert None == ms.push(84)
    assert 84 == ms.peekMax()
    assert None == ms.push(-74)
    assert -74 == ms.pop()
    assert 84 == ms.pop()
    assert None == ms.push(-3)
    assert 60 == ms.peekMax()
    assert None == ms.push(16)
    assert 16 == ms.top()
    assert 60 == ms.popMax()
    assert 16 == ms.pop()
    assert -3 == ms.top()
    assert -3 == ms.pop()
    assert None == ms.push(93)
    assert None == ms.push(-83)
    assert -83 == ms.top()
    assert -83 == ms.pop()
    assert None == ms.push(-14)
    assert None == ms.push(-10)
    assert -10 == ms.pop()
    assert None == ms.push(-44)
    assert None == ms.push(5)
    assert 93 == ms.peekMax()
    assert 5 == ms.top()
    assert 5 == ms.pop()
    assert None == ms.push(-72)
    assert -72 == ms.top()
    assert 93 == ms.popMax()
    assert None == ms.push(-80)
    assert 47 == ms.popMax()
    assert None == ms.push(38)
    assert None == ms.push(-7)
    assert 42 == ms.popMax()
    assert 39 == ms.popMax()
    assert None == ms.push(-54)
    assert None == ms.push(25)
    assert 39 == ms.peekMax()
    assert None == ms.push(-61)
    assert -61 == ms.top()
    assert None == ms.push(-61)
    assert None == ms.push(89)
    assert None == ms.push(38)
    assert 38 == ms.pop()
    assert 89 == ms.peekMax()
    assert 89 == ms.peekMax()
    assert 89 == ms.peekMax()
    assert 89 == ms.peekMax()
    assert None == ms.push(-2)
    assert None == ms.push(-19)
    assert None == ms.push(58)
    assert 58 == ms.top()
    assert 58 == ms.top()
    assert None == ms.push(-32)
    assert None == ms.push(60)
    assert 60 == ms.pop()
    assert 89 == ms.peekMax()
    assert None == ms.push(58)
    assert None == ms.push(-95)
    assert -95 == ms.top()
    assert 89 == ms.peekMax()
    assert 89 == ms.peekMax()
    assert -95 == ms.pop()
    assert 58 == ms.pop()
    assert -32 == ms.top()
    assert 89 == ms.peekMax()
    assert -32 == ms.top()
    assert -32 == ms.top()
    assert None == ms.push(58)
    assert None == ms.push(67)
    assert 89 == ms.popMax()
    assert 67 == ms.top()
    assert 67 == ms.popMax()
    assert 58 == ms.popMax()
    assert None == ms.push(34)
    assert 34 == ms.pop()
    assert -32 == ms.top()
    assert None == ms.push(-52)
    assert 58 == ms.peekMax()
    assert -52 == ms.top()
    assert 58 == ms.popMax()
    assert -52 == ms.pop()
    assert None == ms.push(31)
    assert 39 == ms.popMax()
    assert None == ms.push(12)
    assert None == ms.push(-30)
    assert None == ms.push(99)
    assert None == ms.push(-19)
    assert None == ms.push(21)
    assert 99 == ms.peekMax()
    assert 21 == ms.top()
    assert 21 == ms.top()
    assert 99 == ms.peekMax()
    assert 99 == ms.peekMax()
    assert None == ms.push(-87)
    assert 99 == ms.peekMax()
    assert 99 == ms.peekMax()
    assert -87 == ms.pop()
    assert None == ms.push(68)
    assert 99 == ms.popMax()
    assert 68 == ms.peekMax()
    assert None == ms.push(-29)
    assert 68 == ms.peekMax()
    assert None == ms.push(-79)
    assert -79 == ms.pop()
    assert None == ms.push(-57)
    assert None == ms.push(80)
    assert 80 == ms.pop()
    assert None == ms.push(53)
    assert None == ms.push(15)
    assert 68 == ms.popMax()
    assert 53 == ms.peekMax()
    assert 15 == ms.pop()
    assert 53 == ms.peekMax()
    assert 53 == ms.top()
    assert 53 == ms.popMax()
    assert None == ms.push(18)
    assert 38 == ms.peekMax()
    assert None == ms.push(-95)
    assert None == ms.push(-79)
    assert None == ms.push(30)
    assert 30 == ms.pop()
    assert 38 == ms.popMax()
    assert 36 == ms.peekMax()
    assert None == ms.push(0)
    assert 0 == ms.top()
    assert 36 == ms.peekMax()