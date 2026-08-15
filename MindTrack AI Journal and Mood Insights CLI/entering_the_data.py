import json
from datetime import datetime

admins = {
    1: {"admin_alex": "Admin@92831"},
    2: {"admin_olivia": "Admin@64752"},
    3: {"admin_daniel": "Admin@81539"}
}

developers = {
    1: {"alex_dev": "Dev@48291"},
    2: {"olivia_dev": "Dev@73925"},
    3: {"daniel_dev": "Dev@61583"},
    4: {"emily_dev": "Dev@29476"},
    5: {"james_dev": "Dev@85364"}
}

users = {
    1: {"alex_wilson": "Alex@4821"},
    2: {"olivia_smith": "Olivia@7392"},
    3: {"daniel_brown": "Daniel@6158"},
    4: {"emily_johnson": "Emily@2947"},
    5: {"james_taylor": "James@8536"},
    6: {"sophia_williams": "Sophia@4219"},
    7: {"ethan_davis": "Ethan@7683"},
    8: {"charlotte_miller": "Charlotte@5362"},
    9: {"noah_anderson": "Noah@9174"},
    10: {"ava_thompson": "Ava@3845"},
    11: {"liam_martin": "Liam@6528"},
    12: {"mia_roberts": "Mia@7491"},
    13: {"william_clark": "William@2856"},
    14: {"amelia_lewis": "Amelia@9137"},
    15: {"henry_walker": "Henry@4672"},
    16: {"isla_hall": "Isla@8354"},
    17: {"jack_allen": "Jack@5913"},
    18: {"ella_young": "Ella@7264"},
    19: {"charlie_king": "Charlie@3489"},
    20: {"grace_wright": "Grace@6147"},
    21: {"ahmed_khan": "Ahmed@8293"},
    22: {"ali_raza": "Ali@4751"},
    23: {"hamza_ahmed": "Hamza@6382"},
    24: {"hassan_ali": "Hassan@9146"},
    25: {"usman_khan": "Usman@3578"},
    26: {"zain_raza": "Zain@6824"},
    27: {"bilal_ahmed": "Bilal@5197"},
    28: {"saad_khan": "Saad@8436"},
    29: {"talha_ali": "Talha@2765"},
    30: {"owais_raza": "Owais@7318"},
    31: {"ayesha_khan": "Ayesha@4952"},
    32: {"fatima_ali": "Fatima@8673"},
    33: {"zainab_ahmed": "Zainab@3248"},
    34: {"maryam_khan": "Maryam@7591"},
    35: {"hira_ali": "Hira@6135"},
    36: {"sana_ahmed": "Sana@9482"},
    37: {"laiba_khan": "Laiba@5367"},
    38: {"noor_ali": "Noor@8214"},
    39: {"iqra_ahmed": "Iqra@4679"},
    40: {"maham_khan": "Maham@7358"},
    41: {"david_morgan": "David@5926"},
    42: {"lucas_cooper": "Lucas@8143"},
    43: {"chloe_bennett": "Chloe@3765"},
    44: {"lily_carter": "Lily@9284"},
    45: {"benjamin_hughes": "Benjamin@6417"},
    46: {"harper_reed": "Harper@5832"},
    47: {"logan_foster": "Logan@7196"},
    48: {"zoe_mitchell": "Zoe@4528"},
    49: {"samuel_ward": "Samuel@8361"},
    50: {"ruby_brooks": "Ruby@6947"}
}

user_profiles = {
    1: {
        "name": "Alex Wilson",
        "signup_datetime": "2026-07-01 10:15:00",
        "date_of_birth": "2005-03-18"
    },

    2: {
        "name": "Olivia Smith",
        "signup_datetime": "2026-07-02 14:30:00",
        "date_of_birth": "2004-07-22"
    },

    3: {
        "name": "Daniel Brown",
        "signup_datetime": "2026-07-03 09:45:00",
        "date_of_birth": "2006-11-05"
    },

    4: {
        "name": "Emily Johnson",
        "signup_datetime": "2026-07-04 16:20:00",
        "date_of_birth": "2005-01-27"
    },

    5: {
        "name": "James Taylor",
        "signup_datetime": "2026-07-05 11:10:00",
        "date_of_birth": "2003-09-14"
    },

    6: {
        "name": "Sophia Williams",
        "signup_datetime": "2026-07-06 13:25:00",
        "date_of_birth": "2004-12-09"
    },

    7: {
        "name": "Ethan Davis",
        "signup_datetime": "2026-07-07 08:40:00",
        "date_of_birth": "2005-05-21"
    },

    8: {
        "name": "Charlotte Miller",
        "signup_datetime": "2026-07-08 17:15:00",
        "date_of_birth": "2006-02-11"
    },

    9: {
        "name": "Noah Anderson",
        "signup_datetime": "2026-07-09 12:50:00",
        "date_of_birth": "2003-08-30"
    },

    10: {
        "name": "Ava Thompson",
        "signup_datetime": "2026-07-10 15:35:00",
        "date_of_birth": "2005-10-17"
    },

    11: {
        "name": "Liam Martin",
        "signup_datetime": "2026-07-11 10:20:00",
        "date_of_birth": "2004-04-06"
    },

    12: {
        "name": "Mia Roberts",
        "signup_datetime": "2026-07-12 09:10:00",
        "date_of_birth": "2006-06-25"
    },

    13: {
        "name": "William Clark",
        "signup_datetime": "2026-07-13 14:45:00",
        "date_of_birth": "2002-12-15"
    },

    14: {
        "name": "Amelia Lewis",
        "signup_datetime": "2026-07-14 11:30:00",
        "date_of_birth": "2005-07-03"
    },

    15: {
        "name": "Henry Walker",
        "signup_datetime": "2026-07-15 16:05:00",
        "date_of_birth": "2004-10-28"
    },

    16: {
        "name": "Isla Hall",
        "signup_datetime": "2026-07-16 08:55:00",
        "date_of_birth": "2006-03-19"
    },

    17: {
        "name": "Jack Allen",
        "signup_datetime": "2026-07-17 13:40:00",
        "date_of_birth": "2003-05-12"
    },

    18: {
        "name": "Ella Young",
        "signup_datetime": "2026-07-18 10:05:00",
        "date_of_birth": "2005-11-23"
    },

    19: {
        "name": "Charlie King",
        "signup_datetime": "2026-07-19 15:20:00",
        "date_of_birth": "2004-02-07"
    },

    20: {
        "name": "Grace Wright",
        "signup_datetime": "2026-07-20 12:15:00",
        "date_of_birth": "2006-08-16"
    },

    21: {
        "name": "Ahmed Khan",
        "signup_datetime": "2026-07-21 09:35:00",
        "date_of_birth": "2003-06-02"
    },

    22: {
        "name": "Ali Raza",
        "signup_datetime": "2026-07-22 14:10:00",
        "date_of_birth": "2005-09-11"
    },

    23: {
        "name": "Hamza Ahmed",
        "signup_datetime": "2026-07-23 11:45:00",
        "date_of_birth": "2004-01-30"
    },

    24: {
        "name": "Hassan Ali",
        "signup_datetime": "2026-07-24 16:30:00",
        "date_of_birth": "2006-05-08"
    },

    25: {
        "name": "Usman Khan",
        "signup_datetime": "2026-07-25 10:50:00",
        "date_of_birth": "2003-11-19"
    },

    26: {
        "name": "Zain Raza",
        "signup_datetime": "2026-07-26 13:15:00",
        "date_of_birth": "2005-04-24"
    },

    27: {
        "name": "Bilal Ahmed",
        "signup_datetime": "2026-07-27 09:25:00",
        "date_of_birth": "2004-08-07"
    },

    28: {
        "name": "Saad Khan",
        "signup_datetime": "2026-07-28 15:40:00",
        "date_of_birth": "2006-01-13"
    },

    29: {
        "name": "Talha Ali",
        "signup_datetime": "2026-07-29 11:20:00",
        "date_of_birth": "2003-10-05"
    },

    30: {
        "name": "Owais Raza",
        "signup_datetime": "2026-07-30 17:05:00",
        "date_of_birth": "2005-06-18"
    },

    31: {
        "name": "Ayesha Khan",
        "signup_datetime": "2026-07-01 12:40:00",
        "date_of_birth": "2004-03-27"
    },

    32: {
        "name": "Fatima Ali",
        "signup_datetime": "2026-07-02 10:30:00",
        "date_of_birth": "2006-09-09"
    },

    33: {
        "name": "Zainab Ahmed",
        "signup_datetime": "2026-07-03 14:55:00",
        "date_of_birth": "2005-12-01"
    },

    34: {
        "name": "Maryam Khan",
        "signup_datetime": "2026-07-04 09:20:00",
        "date_of_birth": "2003-07-15"
    },

    35: {
        "name": "Hira Ali",
        "signup_datetime": "2026-07-05 16:45:00",
        "date_of_birth": "2004-05-29"
    },

    36: {
        "name": "Sana Ahmed",
        "signup_datetime": "2026-07-06 11:35:00",
        "date_of_birth": "2006-10-12"
    },

    37: {
        "name": "Laiba Khan",
        "signup_datetime": "2026-07-07 13:50:00",
        "date_of_birth": "2005-02-20"
    },

    38: {
        "name": "Noor Ali",
        "signup_datetime": "2026-07-08 08:30:00",
        "date_of_birth": "2003-12-06"
    },

    39: {
        "name": "Iqra Ahmed",
        "signup_datetime": "2026-07-09 15:15:00",
        "date_of_birth": "2004-06-17"
    },

    40: {
        "name": "Maham Khan",
        "signup_datetime": "2026-07-10 10:45:00",
        "date_of_birth": "2006-04-03"
    },

    41: {
        "name": "David Morgan",
        "signup_datetime": "2026-07-11 12:20:00",
        "date_of_birth": "2002-09-26"
    },

    42: {
        "name": "Lucas Cooper",
        "signup_datetime": "2026-07-12 17:30:00",
        "date_of_birth": "2005-08-14"
    },

    43: {
        "name": "Chloe Bennett",
        "signup_datetime": "2026-07-13 09:50:00",
        "date_of_birth": "2004-11-08"
    },

    44: {
        "name": "Lily Carter",
        "signup_datetime": "2026-07-14 14:25:00",
        "date_of_birth": "2006-02-28"
    },

    45: {
        "name": "Benjamin Hughes",
        "signup_datetime": "2026-07-15 11:55:00",
        "date_of_birth": "2003-04-16"
    },

    46: {
        "name": "Harper Reed",
        "signup_datetime": "2026-07-16 16:10:00",
        "date_of_birth": "2005-07-31"
    },

    47: {
        "name": "Logan Foster",
        "signup_datetime": "2026-07-17 10:35:00",
        "date_of_birth": "2004-01-22"
    },

    48: {
        "name": "Zoe Mitchell",
        "signup_datetime": "2026-07-18 13:05:00",
        "date_of_birth": "2006-06-11"
    },

    49: {
        "name": "Samuel Ward",
        "signup_datetime": "2026-07-19 15:50:00",
        "date_of_birth": "2003-10-21"
    },

    50: {
        "name": "Ruby Brooks",
        "signup_datetime": "2026-07-20 09:40:00",
        "date_of_birth": "2005-05-04"
    }
}

journal_entries = {
    1: {
        "1_1": {
            "date": "2026-07-01",
            "time_stamp": "10:15:00",
            "title": "A Productive Start",
            "journal": "Today I finally finished the project I had been working on. I felt really happy and motivated because everything went better than I expected.",
            "mood_score": 9
        },
        "1_2": {
            "date": "2026-07-04",
            "time_stamp": "18:30:00",
            "title": "Quiet Evening",
            "journal": "I spent the evening at home listening to music and thinking about my goals. It was peaceful and I felt calm.",
            "mood_score": 8
        },
        "1_3": {
            "date": "2026-07-08",
            "time_stamp": "21:10:00",
            "title": "Small Wins",
            "journal": "I managed to complete several small tasks today. They were not huge achievements, but finishing them made me feel good.",
            "mood_score": 8
        }
    },

    2: {
        "2_1": {
            "date": "2026-07-02",
            "time_stamp": "14:20:00",
            "title": "A Difficult Day",
            "journal": "Today was quite stressful. I had several things to finish and felt overwhelmed for most of the afternoon.",
            "mood_score": 3
        },
        "2_2": {
            "date": "2026-07-06",
            "time_stamp": "20:10:00",
            "title": "Things Got Better",
            "journal": "The day started badly, but things slowly improved. I talked with a friend and felt much better afterward.",
            "mood_score": 7
        }
    },

    3: {
        "3_1": {
            "date": "2026-07-03",
            "time_stamp": "09:45:00",
            "title": "Fresh Morning",
            "journal": "I woke up early today and went for a short walk. The fresh air helped me feel energetic and ready for the day.",
            "mood_score": 8
        },
        "3_2": {
            "date": "2026-07-07",
            "time_stamp": "19:25:00",
            "title": "Unexpected Problem",
            "journal": "Something went wrong with my plans today. I was frustrated at first, but I tried to stay patient and solve the problem.",
            "mood_score": 5
        },
        "3_3": {
            "date": "2026-07-11",
            "time_stamp": "22:05:00",
            "title": "Feeling Better",
            "journal": "I had a much better day today. I finished my work and spent some time doing something I enjoy.",
            "mood_score": 8
        },
        "3_4": {
            "date": "2026-07-15",
            "time_stamp": "20:40:00",
            "title": "A Good Memory",
            "journal": "I remembered an old moment that made me smile. It reminded me that some simple memories can make an ordinary day special.",
            "mood_score": 9
        }
    },

    4: {
        "4_1": {
            "date": "2026-07-04",
            "time_stamp": "16:20:00",
            "title": "Learning Something New",
            "journal": "I spent several hours learning something new today. It was difficult at first, but I slowly started understanding it.",
            "mood_score": 8
        },
        "4_2": {
            "date": "2026-07-10",
            "time_stamp": "21:35:00",
            "title": "Long Day",
            "journal": "Today felt longer than usual. I was tired by the evening and decided to rest instead of forcing myself to keep working.",
            "mood_score": 5
        }
    },

    5: {
        "5_1": {
            "date": "2026-07-05",
            "time_stamp": "11:10:00",
            "title": "A Happy Surprise",
            "journal": "Something unexpected happened today and it made me genuinely happy. I spent the rest of the day in a really positive mood.",
            "mood_score": 9
        },
        "5_2": {
            "date": "2026-07-09",
            "time_stamp": "17:45:00",
            "title": "Busy Afternoon",
            "journal": "I had many things to do today and felt a little stressed. Still, I managed to finish most of my responsibilities.",
            "mood_score": 6
        },
        "5_3": {
            "date": "2026-07-14",
            "time_stamp": "20:15:00",
            "title": "Relaxing Night",
            "journal": "I stayed home tonight and watched a movie. It was nice to slow down and enjoy some quiet time.",
            "mood_score": 8
        },
        "5_4": {
            "date": "2026-07-20",
            "time_stamp": "22:00:00",
            "title": "Thinking About Goals",
            "journal": "I spent some time thinking about what I want to accomplish this year. I feel hopeful about the future.",
            "mood_score": 8
        },
        "5_5": {
            "date": "2026-07-25",
            "time_stamp": "19:30:00",
            "title": "A Tired Day",
            "journal": "I felt tired today and did not have much energy. I decided to take things slowly and give myself some rest.",
            "mood_score": 5
        }
    },

    6: {
        "6_1": {
            "date": "2026-07-06",
            "time_stamp": "13:25:00",
            "title": "Feeling Grateful",
            "journal": "I thought about the people who have supported me recently. I feel grateful for having good people around me.",
            "mood_score": 9
        },
        "6_2": {
            "date": "2026-07-12",
            "time_stamp": "18:50:00",
            "title": "A Calm Day",
            "journal": "Nothing unusual happened today, but that was actually nice. I enjoyed having a simple and peaceful day.",
            "mood_score": 8
        }
    },

    7: {
        "7_1": {
            "date": "2026-07-07",
            "time_stamp": "08:40:00",
            "title": "Early Start",
            "journal": "I started my morning earlier than usual. Getting things done early made the rest of the day feel easier.",
            "mood_score": 8
        },
        "7_2": {
            "date": "2026-07-13",
            "time_stamp": "20:25:00",
            "title": "A Little Stress",
            "journal": "I had a few problems to deal with today. I felt stressed for a while, but eventually everything became manageable.",
            "mood_score": 5
        },
        "7_3": {
            "date": "2026-07-18",
            "time_stamp": "21:45:00",
            "title": "Weekend Mood",
            "journal": "I had time to relax and enjoy my weekend. I listened to music and felt completely refreshed.",
            "mood_score": 9
        }
    },

    8: {
        "8_1": {
            "date": "2026-07-08",
            "time_stamp": "17:15:00",
            "title": "Creative Energy",
            "journal": "I spent some time working on a creative idea today. It felt exciting to see something slowly come together.",
            "mood_score": 9
        },
        "8_2": {
            "date": "2026-07-16",
            "time_stamp": "19:20:00",
            "title": "Quiet Thoughts",
            "journal": "I spent the evening thinking about recent changes in my life. I am still figuring things out, but I feel hopeful.",
            "mood_score": 7
        }
    },

    9: {
        "9_1": {
            "date": "2026-07-09",
            "time_stamp": "12:50:00",
            "title": "A Normal Day",
            "journal": "Today was mostly ordinary. I completed my responsibilities and had a little time to relax.",
            "mood_score": 6
        },
        "9_2": {
            "date": "2026-07-17",
            "time_stamp": "21:15:00",
            "title": "Feeling Proud",
            "journal": "I accomplished something I had been putting off for a long time. I am proud that I finally got it done.",
            "mood_score": 9
        },
        "9_3": {
            "date": "2026-07-23",
            "time_stamp": "18:40:00",
            "title": "A Rainy Evening",
            "journal": "The weather was rainy today, so I stayed inside. The sound of rain made the evening feel peaceful.",
            "mood_score": 8
        }
    },

    10: {
        "10_1": {
            "date": "2026-07-10",
            "time_stamp": "15:35:00",
            "title": "A Good Conversation",
            "journal": "I had a really good conversation with someone today. It helped me understand something I had been worrying about.",
            "mood_score": 8
        },
        "10_2": {
            "date": "2026-07-19",
            "time_stamp": "20:05:00",
            "title": "Feeling Motivated",
            "journal": "I made a new plan for my goals today. Writing everything down made me feel motivated to start.",
            "mood_score": 9
        }
    },

    11: {
        "11_1": {
            "date": "2026-07-11",
            "time_stamp": "10:20:00",
            "title": "Focused Morning",
            "journal": "I stayed focused throughout the morning and completed more work than I expected. It felt satisfying.",
            "mood_score": 9
        }
    },

    12: {
        "12_1": {
            "date": "2026-07-12",
            "time_stamp": "09:10:00",
            "title": "Slow Morning",
            "journal": "I had a slow start today. I was tired when I woke up, but eventually I felt better.",
            "mood_score": 6
        },
        "12_2": {
            "date": "2026-07-21",
            "time_stamp": "19:35:00",
            "title": "Better Evening",
            "journal": "The evening was much nicer than the morning. I spent time with family and felt relaxed.",
            "mood_score": 8
        }
    },

    13: {
        "13_1": {
            "date": "2026-07-13",
            "time_stamp": "14:45:00",
            "title": "A New Opportunity",
            "journal": "I came across an interesting opportunity today. I am excited about what it could lead to.",
            "mood_score": 9
        },
        "13_2": {
            "date": "2026-07-22",
            "time_stamp": "21:00:00",
            "title": "Planning Ahead",
            "journal": "I spent the evening organizing my plans for the next few weeks. I feel prepared and hopeful.",
            "mood_score": 8
        },
        "13_3": {
            "date": "2026-07-28",
            "time_stamp": "18:25:00",
            "title": "Unexpected Delay",
            "journal": "One of my plans was delayed today. I was disappointed, but I reminded myself that some things take time.",
            "mood_score": 5
        }
    },

    14: {
        "14_1": {
            "date": "2026-07-14",
            "time_stamp": "11:30:00",
            "title": "Good Progress",
            "journal": "I made good progress on something important today. Seeing the results made me feel confident.",
            "mood_score": 9
        },
        "14_2": {
            "date": "2026-07-24",
            "time_stamp": "20:30:00",
            "title": "Peaceful Night",
            "journal": "I had a peaceful night and finally got some time to myself. It felt good to slow down.",
            "mood_score": 8
        }
    },

    15: {
        "15_1": {
            "date": "2026-07-15",
            "time_stamp": "16:05:00",
            "title": "Learning From Mistakes",
            "journal": "I made a mistake today, but instead of getting upset I tried to understand what went wrong. I learned something useful.",
            "mood_score": 7
        },
        "15_2": {
            "date": "2026-07-26",
            "time_stamp": "19:45:00",
            "title": "Feeling Positive",
            "journal": "Today ended on a positive note. I feel more confident about handling problems when they appear.",
            "mood_score": 8
        }
    },

    16: {
        "16_1": {
            "date": "2026-07-16",
            "time_stamp": "08:55:00",
            "title": "Morning Motivation",
            "journal": "I woke up feeling motivated today. I wrote down my priorities and started working without wasting much time.",
            "mood_score": 9
        },
        "16_2": {
            "date": "2026-07-29",
            "time_stamp": "22:15:00",
            "title": "A Long Evening",
            "journal": "I had a lot on my mind tonight. I felt tired, so I decided to stop working and get some rest.",
            "mood_score": 5
        }
    },

    17: {
        "17_1": {
            "date": "2026-07-17",
            "time_stamp": "13:40:00",
            "title": "A Fun Afternoon",
            "journal": "I spent the afternoon doing something I really enjoy. I laughed a lot and felt genuinely happy.",
            "mood_score": 10
        },
        "17_2": {
            "date": "2026-07-25",
            "time_stamp": "20:20:00",
            "title": "Reflecting",
            "journal": "I thought about how much I have changed recently. I still have things to improve, but I am proud of my progress.",
            "mood_score": 9
        },
        "17_3": {
            "date": "2026-07-30",
            "time_stamp": "18:10:00",
            "title": "A Challenging Task",
            "journal": "The task I worked on today was harder than expected. I became frustrated but kept trying until I understood it.",
            "mood_score": 6
        }
    },

    18: {
        "18_1": {
            "date": "2026-07-18",
            "time_stamp": "10:05:00",
            "title": "A Fresh Perspective",
            "journal": "I looked at an old problem differently today and suddenly found a possible solution. I felt excited and hopeful.",
            "mood_score": 9
        }
    },

    19: {
        "19_1": {
            "date": "2026-07-19",
            "time_stamp": "15:20:00",
            "title": "A Busy Day",
            "journal": "There were many things happening today. I was busy for most of the day but felt satisfied after finishing everything.",
            "mood_score": 7
        },
        "19_2": {
            "date": "2026-07-27",
            "time_stamp": "21:30:00",
            "title": "Resting",
            "journal": "I decided not to push myself today. Resting felt necessary, and I feel more comfortable after taking a break.",
            "mood_score": 7
        }
    },

    20: {
        "20_1": {
            "date": "2026-07-20",
            "time_stamp": "12:15:00",
            "title": "A Simple Day",
            "journal": "Nothing dramatic happened today. I enjoyed a simple routine and felt comfortable with how the day went.",
            "mood_score": 7
        },
        "20_2": {
            "date": "2026-07-31",
            "time_stamp": "19:50:00",
            "title": "Looking Forward",
            "journal": "I have something exciting coming up soon. Thinking about it makes me feel hopeful and energetic.",
            "mood_score": 9
        }
    },

    21: {
        "21_1": {
            "date": "2026-07-21",
            "time_stamp": "09:35:00",
            "title": "A Strong Start",
            "journal": "I started the day with clear goals and managed to stay focused. I felt productive and confident.",
            "mood_score": 9
        },
        "21_2": {
            "date": "2026-07-26",
            "time_stamp": "22:05:00",
            "title": "Quiet Thoughts",
            "journal": "Tonight I thought about some decisions I need to make. I do not have all the answers yet, but I feel calm about it.",
            "mood_score": 7
        }
    },

    22: {
        "22_1": {
            "date": "2026-07-22",
            "time_stamp": "14:10:00",
            "title": "A Helpful Friend",
            "journal": "A friend helped me understand something difficult today. I felt grateful and much less worried afterward.",
            "mood_score": 9
        },
        "22_2": {
            "date": "2026-07-29",
            "time_stamp": "20:45:00",
            "title": "A Small Disappointment",
            "journal": "Something I expected did not happen today. I felt disappointed for a while, but I am trying to stay positive.",
            "mood_score": 5
        },
        "22_3": {
            "date": "2026-07-31",
            "time_stamp": "21:15:00",
            "title": "Ending Well",
            "journal": "The day ended better than it started. I spent some time relaxing and now I feel much more peaceful.",
            "mood_score": 8
        }
    },

    23: {
        "23_1": {
            "date": "2026-07-23",
            "time_stamp": "11:45:00",
            "title": "Getting Things Done",
            "journal": "I had a productive morning and completed several tasks. I feel good knowing that I made progress.",
            "mood_score": 8
        }
    },

    24: {
        "24_1": {
            "date": "2026-07-24",
            "time_stamp": "16:30:00",
            "title": "A Difficult Conversation",
            "journal": "I had a difficult conversation today. It was uncomfortable, but I am glad I was honest about how I felt.",
            "mood_score": 6
        },
        "24_2": {
            "date": "2026-07-30",
            "time_stamp": "20:00:00",
            "title": "Feeling Relieved",
            "journal": "The situation I was worried about has finally been resolved. I feel relieved and much calmer now.",
            "mood_score": 8
        }
    },

    25: {
        "25_1": {
            "date": "2026-07-25",
            "time_stamp": "10:50:00",
            "title": "A Fresh Goal",
            "journal": "I decided on a new goal today. It feels challenging, but I am excited to work toward it.",
            "mood_score": 9
        },
        "25_2": {
            "date": "2026-07-28",
            "time_stamp": "19:15:00",
            "title": "Slow Progress",
            "journal": "Things are moving more slowly than I wanted, but at least I am still making progress.",
            "mood_score": 7
        },
        "25_3": {
            "date": "2026-07-31",
            "time_stamp": "22:20:00",
            "title": "Satisfied",
            "journal": "I looked back at what I accomplished this week. I feel satisfied with the effort I put in.",
            "mood_score": 9
        }
    },

    26: {
        "26_1": {
            "date": "2026-07-26",
            "time_stamp": "13:15:00",
            "title": "A Calm Afternoon",
            "journal": "The afternoon was quiet and comfortable. I had enough time to finish my work without feeling rushed.",
            "mood_score": 8
        },
        "26_2": {
            "date": "2026-07-31",
            "time_stamp": "18:45:00",
            "title": "Good News",
            "journal": "I received some good news today. It immediately improved my mood and gave me more confidence.",
            "mood_score": 9
        }
    },

    27: {
        "27_1": {
            "date": "2026-07-27",
            "time_stamp": "09:25:00",
            "title": "Morning Walk",
            "journal": "I went outside for a short walk this morning. The fresh air helped clear my thoughts and made me feel relaxed.",
            "mood_score": 8
        }
    },

    28: {
        "28_1": {
            "date": "2026-07-28",
            "time_stamp": "15:40:00",
            "title": "Too Much Work",
            "journal": "I had more work than I expected today. I became stressed and tired, so I took several short breaks.",
            "mood_score": 4
        },
        "28_2": {
            "date": "2026-07-30",
            "time_stamp": "21:05:00",
            "title": "Recovering",
            "journal": "I took some time to rest today and feel much better now. Sometimes taking a break is exactly what I need.",
            "mood_score": 7
        }
    },

    29: {
        "29_1": {
            "date": "2026-07-29",
            "time_stamp": "11:20:00",
            "title": "Feeling Confident",
            "journal": "I handled a difficult task without giving up. I feel more confident in my abilities after today.",
            "mood_score": 9
        },
        "29_2": {
            "date": "2026-07-31",
            "time_stamp": "19:40:00",
            "title": "A Peaceful Moment",
            "journal": "I sat quietly for a while and listened to music. It was a small moment, but it made me feel peaceful.",
            "mood_score": 8
        }
    },

    30: {
        "30_1": {
            "date": "2026-07-30",
            "time_stamp": "17:05:00",
            "title": "A Productive Evening",
            "journal": "I completed several tasks this evening. I was tired, but finishing everything gave me a strong sense of accomplishment.",
            "mood_score": 8
        }
    },

    31: {
        "31_1": {
            "date": "2026-07-01",
            "time_stamp": "12:40:00",
            "title": "New Beginnings",
            "journal": "Today felt like a fresh beginning. I have several plans for the future and feel excited about starting them.",
            "mood_score": 9
        },
        "31_2": {
            "date": "2026-07-08",
            "time_stamp": "18:10:00",
            "title": "A Little Uncertain",
            "journal": "I am not completely sure whether I am making the right decision. Still, I am trying to trust myself.",
            "mood_score": 6
        },
        "31_3": {
            "date": "2026-07-19",
            "time_stamp": "21:25:00",
            "title": "Feeling Hopeful",
            "journal": "Things are slowly becoming clearer. I feel more hopeful than I did a few weeks ago.",
            "mood_score": 8
        },
        "31_4": {
            "date": "2026-07-29",
            "time_stamp": "20:15:00",
            "title": "Proud of Myself",
            "journal": "I looked back at everything I managed to accomplish. I am genuinely proud of how far I have come.",
            "mood_score": 10
        }
    },

    32: {
        "32_1": {
            "date": "2026-07-02",
            "time_stamp": "10:30:00",
            "title": "A Busy Morning",
            "journal": "My morning was extremely busy. I had several responsibilities and barely had time to rest.",
            "mood_score": 5
        },
        "32_2": {
            "date": "2026-07-17",
            "time_stamp": "19:10:00",
            "title": "Finally Relaxing",
            "journal": "After a long week, I finally had some free time. I watched something funny and felt much more relaxed.",
            "mood_score": 8
        }
    },

    33: {
        "33_1": {
            "date": "2026-07-03",
            "time_stamp": "14:55:00",
            "title": "Good News",
            "journal": "I heard some wonderful news today. I could not stop smiling and spent the rest of the afternoon feeling excited.",
            "mood_score": 10
        }
    },

    34: {
        "34_1": {
            "date": "2026-07-04",
            "time_stamp": "09:20:00",
            "title": "A Heavy Morning",
            "journal": "I woke up feeling low today. Nothing specific happened, but I had very little energy and wanted to stay alone.",
            "mood_score": 3
        },
        "34_2": {
            "date": "2026-07-12",
            "time_stamp": "20:40:00",
            "title": "Talking Helped",
            "journal": "I talked to someone I trust about how I had been feeling. It helped more than I expected.",
            "mood_score": 7
        },
        "34_3": {
            "date": "2026-07-23",
            "time_stamp": "18:30:00",
            "title": "A Better Week",
            "journal": "This week has been much better. I have been sleeping well and finding more reasons to smile.",
            "mood_score": 9
        }
    },

    35: {
        "35_1": {
            "date": "2026-07-05",
            "time_stamp": "16:45:00",
            "title": "Trying Again",
            "journal": "Something did not work out yesterday, so I decided to try again today. I feel proud that I did not give up.",
            "mood_score": 8
        },
        "35_2": {
            "date": "2026-07-18",
            "time_stamp": "21:00:00",
            "title": "Small Achievement",
            "journal": "I reached a small goal today. It may not seem important to anyone else, but it means a lot to me.",
            "mood_score": 9
        }
    },

    36: {
        "36_1": {
            "date": "2026-07-06",
            "time_stamp": "11:35:00",
            "title": "Feeling Tired",
            "journal": "I did not sleep very well last night and felt tired throughout the day. I hope tomorrow feels easier.",
            "mood_score": 4
        }
    },

    37: {
        "37_1": {
            "date": "2026-07-07",
            "time_stamp": "13:50:00",
            "title": "A Creative Idea",
            "journal": "I suddenly got a creative idea today and immediately started writing down everything I could think of.",
            "mood_score": 9
        },
        "37_2": {
            "date": "2026-07-20",
            "time_stamp": "20:30:00",
            "title": "Making Progress",
            "journal": "The idea I had earlier is slowly becoming something real. I am excited to see where it goes.",
            "mood_score": 9
        },
        "37_3": {
            "date": "2026-07-30",
            "time_stamp": "22:10:00",
            "title": "Feeling Accomplished",
            "journal": "I finished an important part of my project tonight. I feel proud and motivated to continue.",
            "mood_score": 9
        }
    },

    38: {
        "38_1": {
            "date": "2026-07-08",
            "time_stamp": "08:30:00",
            "title": "Peaceful Morning",
            "journal": "The morning was quiet and peaceful. I enjoyed my breakfast and took some time before starting work.",
            "mood_score": 8
        },
        "38_2": {
            "date": "2026-07-24",
            "time_stamp": "19:25:00",
            "title": "A Good Evening",
            "journal": "I spent the evening with people I care about. We talked, laughed, and had a really good time.",
            "mood_score": 9
        }
    },

    39: {
        "39_1": {
            "date": "2026-07-09",
            "time_stamp": "15:15:00",
            "title": "A Challenging Start",
            "journal": "The morning was frustrating because several things went wrong. I tried to stay patient and eventually solved most of them.",
            "mood_score": 5
        },
        "39_2": {
            "date": "2026-07-16",
            "time_stamp": "21:40:00",
            "title": "Feeling Calm",
            "journal": "Tonight I finally feel calm. I put my phone away for a while and spent some quiet time thinking.",
            "mood_score": 8
        },
        "39_3": {
            "date": "2026-07-28",
            "time_stamp": "18:55:00",
            "title": "A Positive Change",
            "journal": "I noticed a positive change in my routine today. I have been taking better care of my time and energy.",
            "mood_score": 9
        },
        "39_4": {
            "date": "2026-07-31",
            "time_stamp": "22:30:00",
            "title": "Grateful Tonight",
            "journal": "Before sleeping, I thought about everything I am grateful for. There are many more good things in my life than I sometimes notice.",
            "mood_score": 10
        }
    },

    40: {
        "40_1": {
            "date": "2026-07-10",
            "time_stamp": "10:45:00",
            "title": "Organizing My Day",
            "journal": "I made a clear schedule this morning. Having everything organized made me feel less stressed.",
            "mood_score": 8
        }
    },

    41: {
        "41_1": {
            "date": "2026-07-11",
            "time_stamp": "12:20:00",
            "title": "A Proud Moment",
            "journal": "I received recognition for something I worked hard on. I felt proud and grateful at the same time.",
            "mood_score": 10
        },
        "41_2": {
            "date": "2026-07-21",
            "time_stamp": "20:35:00",
            "title": "Looking Back",
            "journal": "I spent some time looking at my old goals. I realized that I have achieved more than I thought.",
            "mood_score": 9
        }
    },

    42: {
        "42_1": {
            "date": "2026-07-12",
            "time_stamp": "17:30:00",
            "title": "A Relaxed Day",
            "journal": "Today was slower than usual. I did not rush anything and enjoyed having enough time for myself.",
            "mood_score": 8
        },
        "42_2": {
            "date": "2026-07-27",
            "time_stamp": "21:20:00",
            "title": "New Motivation",
            "journal": "I found some motivation again today. I think I am ready to start working seriously toward my goals.",
            "mood_score": 9
        },
        "42_3": {
            "date": "2026-07-31",
            "time_stamp": "19:45:00",
            "title": "A Meaningful Day",
            "journal": "Something about today felt meaningful. I spent time with someone important to me and appreciated the moment.",
            "mood_score": 9
        }
    },

    43: {
        "43_1": {
            "date": "2026-07-13",
            "time_stamp": "09:50:00",
            "title": "A Little Anxious",
            "journal": "I woke up feeling nervous about something happening later today. I tried to remind myself that I had prepared well.",
            "mood_score": 4
        },
        "43_2": {
            "date": "2026-07-15",
            "time_stamp": "21:10:00",
            "title": "It Went Well",
            "journal": "The thing I was worried about actually went really well. I feel relieved and proud of myself.",
            "mood_score": 9
        }
    },

    44: {
        "44_1": {
            "date": "2026-07-14",
            "time_stamp": "14:25:00",
            "title": "A Normal Afternoon",
            "journal": "I spent the afternoon working on regular tasks. Nothing special happened, but I felt comfortable and productive.",
            "mood_score": 7
        },
        "44_2": {
            "date": "2026-07-25",
            "time_stamp": "20:50:00",
            "title": "Something Funny",
            "journal": "I had a funny conversation today that completely changed my mood. I laughed much more than I expected.",
            "mood_score": 9
        },
        "44_3": {
            "date": "2026-07-30",
            "time_stamp": "21:35:00",
            "title": "Peaceful Ending",
            "journal": "I ended the day with some music and a cup of tea. It was exactly the kind of peaceful evening I needed.",
            "mood_score": 8
        }
    },

    45: {
        "45_1": {
            "date": "2026-07-15",
            "time_stamp": "11:55:00",
            "title": "Hard Work",
            "journal": "I worked hard today even though I did not feel very motivated at first. Finishing my tasks made me feel accomplished.",
            "mood_score": 8
        }
    },

    46: {
        "46_1": {
            "date": "2026-07-16",
            "time_stamp": "16:10:00",
            "title": "A New Idea",
            "journal": "I thought of a new idea while working today. It made me excited because I can already imagine what it could become.",
            "mood_score": 9
        },
        "46_2": {
            "date": "2026-07-23",
            "time_stamp": "20:20:00",
            "title": "Making It Real",
            "journal": "I started turning my idea into something practical. It is still early, but I feel optimistic about it.",
            "mood_score": 8
        }
    },

    47: {
        "47_1": {
            "date": "2026-07-17",
            "time_stamp": "10:35:00",
            "title": "A Frustrating Morning",
            "journal": "Several small problems happened this morning and they started to annoy me. I took a break before continuing.",
            "mood_score": 4
        },
        "47_2": {
            "date": "2026-07-26",
            "time_stamp": "19:55:00",
            "title": "Much Better",
            "journal": "Today was much better. I got some work done, talked to a friend, and ended the evening feeling positive.",
            "mood_score": 8
        },
        "47_3": {
            "date": "2026-07-31",
            "time_stamp": "21:25:00",
            "title": "A Fresh Start",
            "journal": "I feel ready to leave some old worries behind. Tomorrow feels like a chance to start fresh.",
            "mood_score": 9
        }
    },

    48: {
        "48_1": {
            "date": "2026-07-18",
            "time_stamp": "13:05:00",
            "title": "Enjoying the Day",
            "journal": "The weather was nice and I had plenty of time to enjoy myself. I felt relaxed and happy.",
            "mood_score": 9
        },
        "48_2": {
            "date": "2026-07-22",
            "time_stamp": "18:15:00",
            "title": "A Small Worry",
            "journal": "Something has been on my mind recently. I am trying not to overthink it and remind myself that things will work out.",
            "mood_score": 5
        }
    },

    49: {
        "49_1": {
            "date": "2026-07-19",
            "time_stamp": "15:50:00",
            "title": "Feeling Accomplished",
            "journal": "I completed something important today. It took longer than expected, but I am happy that I kept going.",
            "mood_score": 9
        },
        "49_2": {
            "date": "2026-07-27",
            "time_stamp": "20:10:00",
            "title": "A Calm Evening",
            "journal": "I spent the evening reading and listening to music. It was simple, peaceful, and exactly what I needed.",
            "mood_score": 8
        }
    },

    50: {
        "50_1": {
            "date": "2026-07-20",
            "time_stamp": "09:40:00",
            "title": "A Hopeful Morning",
            "journal": "I woke up feeling hopeful about the future. I wrote down a few goals and felt motivated to work toward them.",
            "mood_score": 9
        },
        "50_2": {
            "date": "2026-07-24",
            "time_stamp": "17:25:00",
            "title": "A Challenging Day",
            "journal": "Today was more difficult than I expected. I felt stressed for a while, but I managed to get through everything.",
            "mood_score": 5
        },
        "50_3": {
            "date": "2026-07-29",
            "time_stamp": "21:50:00",
            "title": "Feeling Thankful",
            "journal": "I thought about the good things that happened this month. I feel thankful for the people and opportunities in my life.",
            "mood_score": 9
        },
        "50_4": {
            "date": "2026-07-31",
            "time_stamp": "22:05:00",
            "title": "Ending the Month",
            "journal": "The month had its difficult moments, but it also had many good ones. I am proud of myself for continuing to move forward.",
            "mood_score": 9
        }
    }
}

mood_analysis = {
    "1_1": {
        "mood_score": 9,
        "mood": "happy",
        "mood_line": "Today was honestly one of the best days I've had in a while."
    },
    "1_2": {
        "mood_score": 8,
        "mood": "calm",
        "mood_line": "I felt peaceful today and finally had some time to slow down."
    },
    "1_3": {
        "mood_score": 6,
        "mood": "okay",
        "mood_line": "Nothing special happened today, but overall I felt pretty okay."
    },

    "2_1": {
        "mood_score": 3,
        "mood": "sad",
        "mood_line": "There was so much going on today that I couldn't really relax."
    },
    "2_2": {
        "mood_score": 7,
        "mood": "hopeful",
        "mood_line": "Things are still difficult, but I feel like they might get better soon."
    },

    "3_1": {
        "mood_score": 8,
        "mood": "energetic",
        "mood_line": "I woke up feeling fresh and had a lot of energy today."
    },
    "3_2": {
        "mood_score": 5,
        "mood": "frustrated",
        "mood_line": "I got frustrated with my work, but I tried not to give up."
    },
    "3_3": {
        "mood_score": 8,
        "mood": "calm",
        "mood_line": "The evening was quiet and I finally felt relaxed."
    },
    "3_4": {
        "mood_score": 9,
        "mood": "happy",
        "mood_line": "I remembered something funny today and it instantly lifted my mood."
    },

    "4_1": {
        "mood_score": 8,
        "mood": "motivated",
        "mood_line": "I learned something new today and it made me feel good about my progress."
    },
    "4_2": {
        "mood_score": 5,
        "mood": "tired",
        "mood_line": "I was exhausted by the end of the day and really needed some rest."
    },

    "5_1": {
        "mood_score": 9,
        "mood": "happy",
        "mood_line": "Something unexpected happened today and it completely made my day."
    },
    "5_2": {
        "mood_score": 6,
        "mood": "busy",
        "mood_line": "Today was really busy, but I managed to finish most of what I needed to do."
    },
    "5_3": {
        "mood_score": 8,
        "mood": "relaxed",
        "mood_line": "I spent some time doing things I enjoy and it felt really nice."
    },
    "5_4": {
        "mood_score": 7,
        "mood": "hopeful",
        "mood_line": "I've been thinking about the future lately, and I actually feel hopeful about it."
    },
    "5_5": {
        "mood_score": 5,
        "mood": "tired",
        "mood_line": "I didn't have much energy today, so I decided to take things slowly."
    },

    "6_1": {
        "mood_score": 9,
        "mood": "grateful",
        "mood_line": "I'm really grateful for the people who were there for me today."
    },
    "6_2": {
        "mood_score": 8,
        "mood": "peaceful",
        "mood_line": "Today felt simple and peaceful, and honestly that's all I needed."
    },

    "7_1": {
        "mood_score": 8,
        "mood": "productive",
        "mood_line": "I started the day with a clear plan and got a lot done."
    },
    "7_2": {
        "mood_score": 5,
        "mood": "stressed",
        "mood_line": "I had too many things to handle at once and it became stressful."
    },
    "7_3": {
        "mood_score": 9,
        "mood": "relaxed",
        "mood_line": "I finally had time to relax this weekend and it felt amazing."
    },

    "8_1": {
        "mood_score": 9,
        "mood": "creative",
        "mood_line": "I worked on something creative today and I got completely lost in it."
    },
    "8_2": {
        "mood_score": 7,
        "mood": "hopeful",
        "mood_line": "I've been thinking a lot about what I want next, but I'm still optimistic."
    },

    "9_1": {
        "mood_score": 6,
        "mood": "neutral",
        "mood_line": "It was a pretty normal day with nothing particularly exciting happening."
    },
    "9_2": {
        "mood_score": 9,
        "mood": "proud",
        "mood_line": "I finished something I've been working on for a while and I'm really proud of myself."
    },
    "9_3": {
        "mood_score": 8,
        "mood": "peaceful",
        "mood_line": "The weather was quiet and peaceful today, so I spent some time just enjoying it."
    },

    "10_1": {
        "mood_score": 8,
        "mood": "relieved",
        "mood_line": "I finally talked about something that had been bothering me and I feel lighter now."
    },
    "10_2": {
        "mood_score": 9,
        "mood": "motivated",
        "mood_line": "I wrote down some new goals today and suddenly I feel motivated again."
    },

    "11_1": {
        "mood_score": 9,
        "mood": "focused",
        "mood_line": "I stayed focused today and actually finished everything I planned to do."
    },

    "12_1": {
        "mood_score": 6,
        "mood": "tired",
        "mood_line": "I didn't feel very energetic this morning, but eventually things got better."
    },
    "12_2": {
        "mood_score": 8,
        "mood": "relaxed",
        "mood_line": "I spent some time with my family today and it helped me relax."
    },

    "13_1": {
        "mood_score": 9,
        "mood": "excited",
        "mood_line": "I got an opportunity today that I wasn't expecting, and I'm really excited about it."
    },
    "13_2": {
        "mood_score": 8,
        "mood": "hopeful",
        "mood_line": "Planning everything ahead made me feel much more prepared for what's coming."
    },
    "13_3": {
        "mood_score": 5,
        "mood": "disappointed",
        "mood_line": "The plans didn't work out today, and honestly I was pretty disappointed."
    },

    "14_1": {
        "mood_score": 9,
        "mood": "confident",
        "mood_line": "I've been working hard lately and today I finally started seeing some progress."
    },
    "14_2": {
        "mood_score": 8,
        "mood": "peaceful",
        "mood_line": "I spent some quiet time alone today and it felt really peaceful."
    },

    "15_1": {
        "mood_score": 7,
        "mood": "positive",
        "mood_line": "I made a mistake today, but instead of being upset I tried to learn from it."
    },
    "15_2": {
        "mood_score": 8,
        "mood": "positive",
        "mood_line": "Looking back at today, I think I'm becoming better at handling difficult situations."
    },

    "16_1": {
        "mood_score": 9,
        "mood": "motivated",
        "mood_line": "I woke up motivated and knew exactly what I wanted to accomplish today."
    },
    "16_2": {
        "mood_score": 5,
        "mood": "tired",
        "mood_line": "By the evening my brain was completely tired and I couldn't focus anymore."
    },

    "17_1": {
        "mood_score": 10,
        "mood": "joyful",
        "mood_line": "I laughed so much today that my cheeks actually hurt."
    },
    "17_2": {
        "mood_score": 9,
        "mood": "proud",
        "mood_line": "I've come a long way compared to where I was a year ago, and that makes me proud."
    },
    "17_3": {
        "mood_score": 5,
        "mood": "frustrated",
        "mood_line": "The task was much harder than I expected, and I got really frustrated."
    },

    "18_1": {
        "mood_score": 9,
        "mood": "hopeful",
        "mood_line": "I finally found a possible solution to something I've been struggling with."
    },

    "19_1": {
        "mood_score": 7,
        "mood": "satisfied",
        "mood_line": "It was a busy day, but I'm glad I managed to handle everything."
    },
    "19_2": {
        "mood_score": 7,
        "mood": "relaxed",
        "mood_line": "I took a proper break today and realized how much I needed it."
    },

    "20_1": {
        "mood_score": 7,
        "mood": "content",
        "mood_line": "Nothing extraordinary happened today, but I enjoyed the simple routine."
    },
    "20_2": {
        "mood_score": 9,
        "mood": "excited",
        "mood_line": "I'm really looking forward to what happens next."
    },

    "21_1": {
        "mood_score": 9,
        "mood": "confident",
        "mood_line": "I got a lot of work done today and felt really confident about my progress."
    },
    "21_2": {
        "mood_score": 7,
        "mood": "calm",
        "mood_line": "I don't have all the answers yet, but I'm learning to be okay with that."
    },

    "22_1": {
        "mood_score": 9,
        "mood": "grateful",
        "mood_line": "Talking to my friend today reminded me that I don't have to handle everything alone."
    },
    "22_2": {
        "mood_score": 5,
        "mood": "disappointed",
        "mood_line": "I was hoping things would go differently, so today was a little disappointing."
    },
    "22_3": {
        "mood_score": 8,
        "mood": "peaceful",
        "mood_line": "The day ended much more peacefully than it started, and I'm glad about that."
    },

    "23_1": {
        "mood_score": 8,
        "mood": "productive",
        "mood_line": "I made good progress today and I'm happy with what I managed to accomplish."
    },

    "24_1": {
        "mood_score": 5,
        "mood": "uneasy",
        "mood_line": "That conversation was difficult and I've been thinking about it ever since."
    },
    "24_2": {
        "mood_score": 8,
        "mood": "relieved",
        "mood_line": "I'm glad we finally talked things through because I feel much better now."
    },

    "25_1": {
        "mood_score": 9,
        "mood": "excited",
        "mood_line": "I set myself a new goal today and I'm genuinely excited to work toward it."
    },
    "25_2": {
        "mood_score": 7,
        "mood": "hopeful",
        "mood_line": "Progress has been slow, but I don't want to give up yet."
    },
    "25_3": {
        "mood_score": 9,
        "mood": "satisfied",
        "mood_line": "I finished what I promised myself I'd do today, and that feels really good."
    },

    "26_1": {
        "mood_score": 8,
        "mood": "calm",
        "mood_line": "I didn't rush myself today and everything felt much more manageable."
    },
    "26_2": {
        "mood_score": 9,
        "mood": "happy",
        "mood_line": "I got some really good news today and it completely changed my mood."
    },

    "27_1": {
        "mood_score": 8,
        "mood": "relaxed",
        "mood_line": "I went for a walk today and it helped clear my head."
    },

    "28_1": {
        "mood_score": 4,
        "mood": "stressed",
        "mood_line": "I had way too much work today and by the end I felt completely drained."
    },
    "28_2": {
        "mood_score": 7,
        "mood": "relieved",
        "mood_line": "After taking some time to rest, I finally started feeling like myself again."
    },

    "29_1": {
        "mood_score": 9,
        "mood": "confident",
        "mood_line": "I managed to solve something difficult today and it gave me a huge confidence boost."
    },
    "29_2": {
        "mood_score": 8,
        "mood": "peaceful",
        "mood_line": "I sat quietly for a while tonight and enjoyed having no pressure on me."
    },

    "30_1": {
        "mood_score": 8,
        "mood": "accomplished",
        "mood_line": "Today was tiring, but I'm happy that I finished everything I needed to finish."
    },

    "31_1": {
        "mood_score": 9,
        "mood": "excited",
        "mood_line": "Starting something new feels scary, but I'm also really excited about it."
    },
    "31_2": {
        "mood_score": 5,
        "mood": "uncertain",
        "mood_line": "I keep questioning whether I made the right decision."
    },
    "31_3": {
        "mood_score": 8,
        "mood": "hopeful",
        "mood_line": "Things are slowly becoming clearer, and I'm starting to feel more hopeful."
    },
    "31_4": {
        "mood_score": 10,
        "mood": "proud",
        "mood_line": "I'm genuinely proud of myself for making it this far."
    },

    "32_1": {
        "mood_score": 5,
        "mood": "tired",
        "mood_line": "My morning was packed with things to do and I already feel tired."
    },
    "32_2": {
        "mood_score": 8,
        "mood": "relaxed",
        "mood_line": "Having some free time today helped me recharge."
    },

    "33_1": {
        "mood_score": 10,
        "mood": "joyful",
        "mood_line": "I got some amazing news today and I couldn't stop smiling."
    },

    "34_1": {
        "mood_score": 3,
        "mood": "sad",
        "mood_line": "Today was one of those days where I just didn't feel like myself."
    },
    "34_2": {
        "mood_score": 7,
        "mood": "relieved",
        "mood_line": "Talking about what I was feeling actually helped me feel a little lighter."
    },
    "34_3": {
        "mood_score": 9,
        "mood": "happy",
        "mood_line": "I've been trying to build a better routine and I think it's finally working."
    },

    "35_1": {
        "mood_score": 8,
        "mood": "determined",
        "mood_line": "Things didn't go as planned, but I'm proud that I kept going."
    },
    "35_2": {
        "mood_score": 9,
        "mood": "proud",
        "mood_line": "I finally achieved something I've been working toward for a long time."
    },

    "36_1": {
        "mood_score": 4,
        "mood": "tired",
        "mood_line": "I barely slept last night and I could feel it affecting everything today."
    },

    "37_1": {
        "mood_score": 9,
        "mood": "creative",
        "mood_line": "I had a new idea today and suddenly I couldn't stop thinking about it."
    },
    "37_2": {
        "mood_score": 9,
        "mood": "excited",
        "mood_line": "Seeing the idea actually start to work was such an exciting feeling."
    },
    "37_3": {
        "mood_score": 9,
        "mood": "accomplished",
        "mood_line": "I finished an important part of my project today and I'm really happy with it."
    },

    "38_1": {
        "mood_score": 8,
        "mood": "peaceful",
        "mood_line": "The morning was quiet and slow, which was exactly what I needed."
    },
    "38_2": {
        "mood_score": 9,
        "mood": "happy",
        "mood_line": "I spent time with people I care about today and it made me really happy."
    },

    "39_1": {
        "mood_score": 5,
        "mood": "frustrated",
        "mood_line": "Everything seemed to go wrong this morning and it honestly annoyed me."
    },
    "39_2": {
        "mood_score": 8,
        "mood": "calm",
        "mood_line": "I took some time away from everything and finally felt calm again."
    },
    "39_3": {
        "mood_score": 9,
        "mood": "positive",
        "mood_line": "I've made a few small changes to my routine and I'm already noticing a difference."
    },
    "39_4": {
        "mood_score": 10,
        "mood": "grateful",
        "mood_line": "Sometimes I forget how many good things I actually have in my life."
    },

    "40_1": {
        "mood_score": 8,
        "mood": "organized",
        "mood_line": "Having everything planned out made me feel much more in control today."
    },

    "41_1": {
        "mood_score": 10,
        "mood": "proud",
        "mood_line": "Someone noticed how hard I've been working, and that meant a lot to me."
    },
    "41_2": {
        "mood_score": 9,
        "mood": "grateful",
        "mood_line": "Looking back at everything I've accomplished makes me realize how much I've grown."
    },

    "42_1": {
        "mood_score": 8,
        "mood": "relaxed",
        "mood_line": "Today moved at a slower pace and I really enjoyed that."
    },
    "42_2": {
        "mood_score": 9,
        "mood": "motivated",
        "mood_line": "I feel ready to put in the work and make progress toward my goals."
    },
    "42_3": {
        "mood_score": 9,
        "mood": "grateful",
        "mood_line": "I had a really meaningful conversation today and I'm grateful for it."
    },

    "43_1": {
        "mood_score": 4,
        "mood": "anxious",
        "mood_line": "I've been nervous about what comes next and I can't stop thinking about it."
    },
    "43_2": {
        "mood_score": 9,
        "mood": "relieved",
        "mood_line": "Everything turned out better than I expected and I finally feel relieved."
    },

    "44_1": {
        "mood_score": 7,
        "mood": "content",
        "mood_line": "It wasn't a particularly exciting day, but I'm satisfied with how it went."
    },
    "44_2": {
        "mood_score": 9,
        "mood": "joyful",
        "mood_line": "I had such a funny conversation today that I kept laughing about it afterward."
    },
    "44_3": {
        "mood_score": 8,
        "mood": "peaceful",
        "mood_line": "I ended the day quietly and it felt good to finally switch off."
    },

    "45_1": {
        "mood_score": 8,
        "mood": "accomplished",
        "mood_line": "The work was difficult, but finishing it made me feel like all the effort was worth it."
    },

    "46_1": {
        "mood_score": 9,
        "mood": "excited",
        "mood_line": "I came up with an idea today that I'm actually really excited about."
    },
    "46_2": {
        "mood_score": 8,
        "mood": "optimistic",
        "mood_line": "I think this idea could become something useful if I keep working on it."
    },

    "47_1": {
        "mood_score": 4,
        "mood": "frustrated",
        "mood_line": "So many little things went wrong today and I was honestly getting annoyed."
    },
    "47_2": {
        "mood_score": 8,
        "mood": "positive",
        "mood_line": "Things got better later in the day and talking to a friend helped a lot."
    },
    "47_3": {
        "mood_score": 9,
        "mood": "hopeful",
        "mood_line": "I'm ready to leave today's problems behind and start fresh tomorrow."
    },

    "48_1": {
        "mood_score": 9,
        "mood": "happy",
        "mood_line": "The day was simple and pleasant, and I felt pretty happy by the evening."
    },
    "48_2": {
        "mood_score": 5,
        "mood": "worried",
        "mood_line": "There's something on my mind that I can't seem to stop worrying about."
    },

    "49_1": {
        "mood_score": 9,
        "mood": "accomplished",
        "mood_line": "I finally completed something important today and it felt amazing."
    },
    "49_2": {
        "mood_score": 8,
        "mood": "peaceful",
        "mood_line": "I spent the evening reading and listening to music, and it was really peaceful."
    },

    "50_1": {
        "mood_score": 9,
        "mood": "hopeful",
        "mood_line": "I feel hopeful about the future and I'm ready to work for what I want."
    },
    "50_2": {
        "mood_score": 5,
        "mood": "stressed",
        "mood_line": "Today was challenging, but I managed to get through it without giving up."
    },
    "50_3": {
        "mood_score": 9,
        "mood": "grateful",
        "mood_line": "I'm thankful for the people and opportunities I have right now."
    },
    "50_4": {
        "mood_score": 9,
        "mood": "proud",
        "mood_line": "When I look back at everything I've overcome, I feel proud of myself."
    }
}

default_stop_words = list({
    "the", "is", "a", "an", "and", "or",
    "but", "to", "of", "in", "on", "for",
    "with", "my", "me", "i", "it", "this",
    "that", "was", "were", "am", "are"
})

user_defined_stop_words = list({
    "today",
    "day",
    "felt",
    "feel",
    "feeling",
    "really",
    "spent",
    "time",
    "things",
    "something",
    "someone",
    "everything",
    "finally",
    "morning",
    "evening",
    "work",
    "working",
    "worked",
    "good",
    "better",
    "little",
    "much",
    "some",
    "want",
    "think",
    "thought",
    "made",
    "make",
    "helped",
    "help",
    "started",
    "start",
    "finished",
    "finish",
    "felt",
    "trying",
    "tried",
    "going",
    "went",
    "spent",
    "enjoyed",
    "enjoy",
    "time"
})

all_stop_words = list(set(default_stop_words + user_defined_stop_words))

mood_scores = {
    "happy": 9,
    "excited": 10,
    "joyful": 9,
    "grateful": 9,
    "calm": 8,
    "content": 8,
    "hopeful": 8,
    "motivated": 8,
    "good": 7,
    "relaxed": 7,
    "okay": 6,
    "neutral": 5,
    "tired": 5,
    "bored": 4,
    "lonely": 4,
    "worried": 4,
    "overwhelmed":4,
    "stressed": 3,
    "sad": 3,
    "angry": 2,
    "frustrated": 2,
    "hopeless": 2,
    "miserable": 1
}


def accessing_the_log_files(filename):
    try:
        with open(filename,"r",encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        message =f"\"{filename}\"  not found"
        print(f"\"{filename}\"  not found")
        data = {}
    except json.JSONDecodeError:
        message = f"\"{filename}\" corrupted"
        print(f"\"{filename}\" corrupted")
        data = {}
    else:
        message = f"\"{filename}\" loaded successfully"
        print(f"\"{filename}\" loaded successfully")
        return data

staff_logs_file = accessing_the_log_files("staff_logs_file.JSON")
print("\n")
users_logs_file = accessing_the_log_files("users_logs_file.JSON")
print("\n")      
        
def entering_the_data(data,filename,entry):
    global staff_logs_file
    try:
        with open(filename,"w",encoding="utf-8") as file:
            json.dump(data,file, indent=4, ensure_ascii=False)
    except FileExistsError:
        message = f"\"{filename}\" already exists"
        print(f"\"{filename}\" already exists")
    except TypeError:
        message = f"""\"{filename}\" corrupted
        \"{filename}\" not in JSON format"""
        print(f"""\"{filename}\" corrupted
        \"{filename}\" not in JSON format""")
    else:
        message = f"\"{filename}\" saved successfully"
        print(f"\"{filename}\" saved successfully")
    finally:
        time_stamp = datetime.now().strftime("%D %H:%M:%S")
        id = len(staff_logs_file) + 1
        if(entry == True):
            staff_logs_file.update({id:{"staff_id": id,
                                        "file_name": f"{filename}",
                                        "time_stamp": time_stamp,
                                        "message": message}})
        else:
            staff_logs_file.update({id:{"staff_id": 00,
                                        "file_name": f"{filename}",
                                        "time_stamp": time_stamp,
                                        "message": message}})

        
def accessing_the_user_data(filename,u_id,staff):
    global staff_logs_file
    global users_logs_file
    try:
        with open(filename,"r",encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        message = f"""\"{filename}\" corrupted
        \"{filename}\" is not in a JSON format"""
        data = {}
    except FileNotFoundError:
        message = f"\"{filename}\" not found"
        data = {}
    else:
        message = f"\"{filename}\" loaded successfully"
    finally:
        time_stamp = datetime.now().strftime("%D %H:%M:%S")
        if(staff == True):
            id = len(staff_logs_file) + 1
            staff_logs_file.update({id:{"staff_id":u_id,
                                        "file_name": f"{filename}",
                                        "time_stamp": time_stamp,
                                        "message": message}})
        else:
            id = len(users_logs_file) + 1
            users_logs_file.update({id:{"user_id":u_id,
                                        "file_name": f"{filename}",
                                        "time_stamp": time_stamp,
                                        "message": message}}) 
    return data

def closing_the_log_files(data,filename):
    with open(filename,"w",encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        message = f"\"{filename}\" saved successfully"
        print(f"\"{filename}\" saved successfully")
    

if __name__  == "__main__":
    staff_logs_file = accessing_the_log_files("staff_logs_file.JSON")
    print("\n")

    users_logs_file = accessing_the_log_files("users_logs_file.JSON")
    print("\n")

    entering_the_data(admins,"admins.JSON",False)
    print("\n")

    entering_the_data(developers,"developers.JSON",False)
    print("\n")

    entering_the_data(users,"users.JSON",False)
    print("\n")

    entering_the_data(user_profiles,"user_profiles.JSON",False)
    print("\n")

    entering_the_data(journal_entries,"journal_entries.JSON",False)
    print("\n")

    entering_the_data(default_stop_words,"default_stop_words.JSON",False)
    print("\n")

    entering_the_data(user_defined_stop_words,"user_defined_stop_words.JSON",False)
    print("\n")

    entering_the_data(all_stop_words,"all_stop_words.JSON",False)
    print("\n")

    entering_the_data(mood_scores,"mood_scores.JSON",False)
    print("\n")

    entering_the_data(mood_analysis,"mood_analysis.JSON",False)
    print("\n")

    closing_the_log_files(staff_logs_file,"staff_logs_file.JSON")

