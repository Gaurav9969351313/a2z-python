corsAllowedUrl = 'http://localhost:4200'

mongoDBURL = "mongodb://localhost:27017/chatbotApiDB"

appName = "MHR_BOT"

landingPageLinks = { "headcount":{ "name":"Head Count", "appID":""}, 
                    "attrition":{ "name":"Attrition", "appID":""}, 
                    "newjoineereport":{ "name":"New Joinee Report", "appID":""}, 
                    "rehirereport":{ "name":"RE Hire Report","appID":""}, 
                    "genderdiversity":{ "name":"Gender diversity", "appID":""}, 
                    "seprationandretirement":{ "name":"Separation And Retirement Report", "appID":""}, 
                    "retirement":{ "name":"Retirement", "appID":""}, 
                    "managerwithhighestattrition":{ "name":"Manager with highest attrition","appID":""}, 
                    "milestoneworkanniverseryreport":{ "name":"Milestone Work Anniversery Report", "appID":""}, 
                    "birthdayreport":{ "name":"Birthday Report", "appID":""}, 
                    "educationalqualificationreport":{ "name":"Educational Qualification Report","appID":""}, 
                    "employeemovementreport":{ "name":"Employee Movement Report", "appID":""}, 
                    "rwsanctionsreport":{ "name":"RW Sanctions Report", "appID":""}, 
                    "employeeconfirmationreport":{ "name":"Employee Confirmation Report","appID":""}, 
                    "performancemanagementreport":{ "name":"Performance Management Report", "appID":""}, 
                    "rewardsandrecognitionreport":{ "name":"Rewards And Recognition Report", "appID":""}, 
                    "regrettableattrition":{ "name":"Regrettable Attrition","appID":""} 
                   }


demoButtons = ["Straight Chart by Dim1","Sales By Region"]

# First Level
firstSetBtns = ["Permanent", "Probationer", "Trainee", "Contract", "Others", "All"]

# Second Level
secondSetBtns = ["Sector", "Business Unit", "Division", "Sub Division", "Department", "Sub Department", "Business Function", "Location"]

# Third Level
thirdSetBtns = ["Gender", "Tenure", "Age", "Band"]

btnsByIndent = {
                    "headcount":{"btns": demoButtons }, 
                    "attrition":{"btns": firstSetBtns },
                    "newjoineereport":{"btns": firstSetBtns },
                    "rehirereport":{"btns": firstSetBtns },
                    "genderdiversity":{"btns": firstSetBtns },
                    "seprationandretirement":{"btns": firstSetBtns },
                    "retirement":{"btns": firstSetBtns },
                    "managerwithhighestattrition":{"btns": firstSetBtns },
                    "milestoneworkanniverseryreport":{"btns": firstSetBtns },
                    "birthdayreport":{"btns": firstSetBtns },
                    "educationalqualificationreport":{"btns": firstSetBtns },
                    "employeemovementreport":{"btns": firstSetBtns },
                    "rwsanctionsreport":{"btns": firstSetBtns },
                    "employeeconfirmationreport":{"btns": firstSetBtns },
                    "performancemanagementreport":{"btns": firstSetBtns },
                    "rewardsandrecognitionreport":{"btns": firstSetBtns },
                    "regrettableattrition":{"btns": firstSetBtns },

                    "permanent":{"btns":secondSetBtns},
                    "probationer":{"btns":secondSetBtns},
                    "trainee":{"btns":secondSetBtns},
                    "contract":{"btns":secondSetBtns},
                    "others":{"btns":secondSetBtns},
                    "all":{"btns":secondSetBtns},

                    "sector":{"btns":thirdSetBtns}, 
                    "businessunit":{"btns":thirdSetBtns},
                    "division":{"btns":thirdSetBtns}, 
                    "subdivision":{"btns":thirdSetBtns}, 
                    "department":{"btns":thirdSetBtns}, 
                    "subdepartment":{"btns":thirdSetBtns}, 
                    "businessfunction":{"btns":thirdSetBtns}, 
                    "location":{"btns":thirdSetBtns}
                }
