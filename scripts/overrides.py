# Hand-adjudicated model_name values that the family table could not classify.
# MOVE: a genuine individual airframe name - it becomes aircraft_name and the
#       family name takes over model_name.
MOVE = {
    40:"Shoo Shoo Baby", 41:"Bockscar", 42:"Enola Gay", 31009:"Mei-Ling",
    3180:"Sally Rand", 22597:"Miss Jacy", 31543:"Avion Pinocho",
    26390:"El Kabong", 25352:"Friendship 7", 28075:"Nagansky expres",
    28058:"Mana", 28059:"Zuzka", 28060:"Matylda", 7031:"Apollo 7",
    17989:"BTS-002", 8249:"Looking Glass", 4238:"ARIA",
    7197:"Shuttle Training Aircraft", 4240:"Total In-Flight Simulator",
    26391:"Primate Capsule", 7540:"Gemini VI-A",
}
# REPLACE: model_name held a designation, a description or a generic word.
# The family name replaces it; nothing moves to aircraft_name.
REPLACE = {
    2004,2005,8616,27615,27616,27732,24118,31396,20597,25302,31112,31113,31467,
    31722,31723,9951,31687,31338,7524,19403,19517,20868,20869,16045,31444,19622,
    31692,30516,14700,14701,14702,14703,20282,15331,28690,14714,16052,14689,
    14690,14691,14692,15623,16040,16036,16037,14396,14685,16018,15209,16063,
    14704,14705,14706,14707,14708,14709,15631,14257,17660,7545,7736,7737,
    14297,14549,15639,16432,7708,20292,23998,25706,20259,
}
