this is an application to scrape trumps tweets.

built using python and playwright

structure of RELEVANT json data received from truth social endpoint

example data:

{
        "id": "116731447139970106", - POST ID
        "created_at": "2026-06-11T12:22:08.864Z", - TIME OF UPLOAD
        "uri": "https://truthsocial.com/@realDonaldTrump/116731447139970106", - LINK TO POST
        "url": "https://truthsocial.com/@realDonaldTrump/116731447139970106", - LINK TO POST
        "content": "<p>The United States will be hitting Iran (Whose Navy, Air Force, Radar, Anti Aircraft, and all other forms of Defense, together with most of its offensive capability, are GONE!), VERY HARD TONIGHT. At some point in the not too distant  future, we will be taking Kharg Island, and other oil infrastructure points, and assume total control of their Oil and Gas Markets, much like we have with Venezuela, which is working out brilliantly for both Venezuela and the United States of America. Thank you for your attention to this matter! President DONALD J. TRUMP</p>", - HTML FOR HIS POST
        "account": { - OBJECT CONTAINING USER DETAILS
            "id": "107780257626128497",
            "username": "realDonaldTrump",
            "acct": "realDonaldTrump",
            "display_name": "Donald J. Trump",
            "locked": false,
            "bot": false,
            "discoverable": false,
            "group": false,
            "created_at": "2022-02-11T16:16:57.705Z",
            "note": "<p></p>",
            "url": "https://truthsocial.com/@realDonaldTrump",
            "avatar": "https://static-assets-1.truthsocial.com/tmtg:prime-ts-assets/accounts/avatars/107/780/257/626/128/497/original/454286ac07a6f6e6.jpeg",
            "avatar_static": "https://static-assets-1.truthsocial.com/tmtg:prime-ts-assets/accounts/avatars/107/780/257/626/128/497/original/454286ac07a6f6e6.jpeg",
            "header": "https://static-assets-1.truthsocial.com/tmtg:prime-ts-assets/accounts/headers/107/780/257/626/128/497/original/ba3b910ba387bf4e.jpeg",
            "header_static": "https://static-assets-1.truthsocial.com/tmtg:prime-ts-assets/accounts/headers/107/780/257/626/128/497/original/ba3b910ba387bf4e.jpeg",
            "followers_count": 12790264,
            "following_count": 69,
            "statuses_count": 34222,
            "last_status_at": "2026-06-12",
            "verified": true,
            "location": "",
            "website": "www.DonaldJTrump.com",
            "unauth_visibility": true,
            "chats_onboarded": true,
            "feeds_onboarded": true,
            "accepting_messages": false,
            "show_nonmember_group_statuses": false,
            "emojis": [],
            "fields": [],
            "tv_onboarded": false,
            "tv_account": false,
            "premium": true
        },
        "media_attachments": [],
        "mentions": [],
        "tags": [],
        "card": null,
        "group": null,
        "quote": null,
        "in_reply_to": null,
        "votable": false,
        "edited_at": null,
        "version": "1",
        "editable": false,
        "title": null,
    },


