def joinAList(listname):
    return {
                "$reduce":{
                    "input":"$"+listname,
                    "initialValue":"",
                    "in":{
                        "$concat":[
                            "$$value",
                            {"$cond":[{"$eq":["$$value",""]},"",";"]},
                            {"$toString":"$$this"}
                        ]
                    }
                }
            }

