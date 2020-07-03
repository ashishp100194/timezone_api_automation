from BaseClass import BaseClass
from Variables import Variables

def test_Get_Time_Zone_TC1():
    Base=BaseClass()
    Base.Timezone("Get_Time_Zone", "Get_Time_Zone_TC1")

def test_Get_Time_Zone_TC2():
    Base=BaseClass()
    Base.Timezone("Get_Time_Zone", "Get_Time_Zone_TC2")

def test_Get_Time_Zone_TC3():
    Base=BaseClass()
    Base.Timezone("Get_Time_Zone", "Get_Time_Zone_TC3")

def test_Get_Time_Zone_TC4():
    Base=BaseClass()
    Base.Timezone("Get_Time_Zone", "Get_Time_Zone_TC4")

def test_Get_Time_Zone_TC5():
    Base=BaseClass()
    Base.Timezone("Get_Time_Zone", "Get_Time_Zone_TC5")

def test_Get_Time_Zone_TC6():
    Base=BaseClass()
    Base.Timezone("Get_Time_Zone", "Get_Time_Zone_TC6")

def test_Get_Time_Zone_TC7():
    Base=BaseClass()
    Base.Timezone("Get_Time_Zone", "Get_Time_Zone_TC7")

def test_Get_Time_Zone_TC8():
    Base=BaseClass()
    Base.Timezone("Get_Time_Zone", "Get_Time_Zone_TC8", Variables["vpi_api_base_url"])

def test_Get_Time_Zone_TC9():
    Base=BaseClass()
    Base.Timezone("Get_Time_Zone", "Get_Time_Zone_TC9", Variables["vpi_api_base_url"])

def test_Get_Time_Zone_TC10():
    Base=BaseClass()
    Base.Timezone("Get_Time_Zone", "Get_Time_Zone_TC10", Variables["vpi_api_base_url"])

def execute_Get_Time_Zone():
    test_Get_Time_Zone_TC1()
    test_Get_Time_Zone_TC2()
    test_Get_Time_Zone_TC3()
    test_Get_Time_Zone_TC4()
    test_Get_Time_Zone_TC5()
    test_Get_Time_Zone_TC6()
    test_Get_Time_Zone_TC7()
    test_Get_Time_Zone_TC8()
    test_Get_Time_Zone_TC9()
    test_Get_Time_Zone_TC10()

execute_Get_Time_Zone()
