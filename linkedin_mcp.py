from fastmcp import FastMCP, mcp_tool
import requests
import json


app = FastMCP("LinkedIn Poster")

ACCESS_TOKEN = ""


def get_linkedin_author_urn():
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    me_url = "https://api.linkedin.com/v2/userinfo"
    response = requests.get(me_url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        linkedin_id = user_data["sub"]
        print(f"✅ Got LinkedIn user ID: {linkedin_id}")
        return f"urn:li:person:{linkedin_id}"
    else:
        print("❌ Failed to fetch user profile")
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        return None


@mcp_tool()
def create_linkedin_post(post_text: str) -> str:
    """
    🧠 Creates a new LinkedIn post using your access token and the user’s URN.
    Args:
        post_text (str): The text content to post on LinkedIn.
    """
    author_urn = get_linkedin_author_urn()
    if not author_urn:
        return "❌ Could not get LinkedIn URN. Check your access token."

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    data = {
        "author": author_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": post_text},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    url = "https://api.linkedin.com/v2/ugcPosts"
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 201:
        return f"✅ Post created successfully!\n{json.dumps(response.json(), indent=2)}"
    else:
        return f"❌ Failed to create post\nStatus Code: {response.status_code}\nResponse: {response.text}"


# 🏃 تشغيل MCP server
if __name__ == "__main__":
    app.run(
        transport="streamable-http",
                    host="0.0.0.0",
                    port=8012,
    )
