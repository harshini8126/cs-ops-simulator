TASKS = {

    "easy": {
        "time_limit": 3,
        "emails": [
            {
                "id": "e1",
                "subject": "Refund request",
                "body": "I was charged twice for my subscription on March 10th. Please process a refund as soon as possible.",
                "customer_id": "c1",
                "urgency": 5
            }
        ],
        "gold": {
            "e1": {
                "category": "billing",
                "priority": "high",
                "decision": "refund"
            }
        }
    },

    "medium": {
        "time_limit": 4,
        "emails": [
            {
                "id": "e2",
                "subject": "App crash",
                "body": "The app crashes every time I try to log in after the latest update. This is blocking my work.",
                "customer_id": "c2",
                "urgency": 4
            },
            {
                "id": "e3",
                "subject": "Payment issue",
                "body": "My payment failed but the amount was deducted from my bank account. Please check and refund.",
                "customer_id": "c3",
                "urgency": 5
            },
            {
                "id": "e4",
                "subject": "General question",
                "body": "I want to update my profile picture but I cannot find the option in settings. Can you help?",
                "customer_id": "c4",
                "urgency": 2
            }
        ],
        "gold": {
            "e2": {
                "category": "technical",
                "priority": "high",
                "decision": "escalate"
            },
            "e3": {
                "category": "billing",
                "priority": "high",
                "decision": "refund"
            },
            "e4": {
                "category": "general",
                "priority": "low",
                "decision": "reply"
            }
        }
    },

    "hard": {
        "time_limit": 5,
        "emails": [
            {
                "id": "e5",
                "subject": "Charged twice and app not working",
                "body": "I was charged twice and the app is also not opening. I already contacted support but no response yet.",
                "customer_id": "c5",
                "urgency": 5
            },
            {
                "id": "e6",
                "subject": "Spam offer",
                "body": "Congratulations! You have won a lottery. Click here to claim your prize.",
                "customer_id": "c6",
                "urgency": 1
            },
            {
                "id": "e7",
                "subject": "Slow performance",
                "body": "The app has been very slow since the last update and it affects my daily usage.",
                "customer_id": "c7",
                "urgency": 3
            },
            {
                "id": "e8",
                "subject": "Refund not processed",
                "body": "I requested a refund last week but have not received it yet. Please update the status.",
                "customer_id": "c8",
                "urgency": 5
            },
            {
                "id": "e9",
                "subject": "Feature request",
                "body": "It would be great if you could add a dark mode feature in the next update.",
                "customer_id": "c9",
                "urgency": 1
            }
        ],
        "gold": {
            "e5": {
                "category": "billing",
                "priority": "high",
                "decision": "refund"
            },
            "e6": {
                "category": "spam",
                "priority": "low",
                "decision": "ignore"
            },
            "e7": {
                "category": "technical",
                "priority": "medium",
                "decision": "escalate"
            },
            "e8": {
                "category": "billing",
                "priority": "high",
                "decision": "refund"
            },
            "e9": {
                "category": "general",
                "priority": "low",
                "decision": "reply"
            }
        }
    }
}