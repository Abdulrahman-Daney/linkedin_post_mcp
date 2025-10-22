# 🚀 LinkedIn Post MCP

A lightweight **MCP tool** that lets you create LinkedIn posts through the official API using **OAuth 2.0** authentication.

## ✨ Features
- Create LinkedIn text posts
- Uses `/v2/userinfo` for user identity
- Built with **FastMCP**
- Runs on `streamable-http` transport (port **8012**)

## ⚙️ Setup
1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/linkedin_post_mcp.git
   cd linkedin_post_mcp
Install dependencies:

bash
Copy code
pip install fastmcp requests
Add your LinkedIn Access Token in linkedin_mcp.py:

python
Copy code
ACCESS_TOKEN = "your_access_token_here"
Run the MCP server:

bash
Copy code
python linkedin_mcp.py
🧠 Usage
Call the MCP tool’s function:

python
Copy code
create_linkedin_post(post_text="🚀 Hello LinkedIn from MCP!")
🔒 Scopes Required
Make sure your LinkedIn app includes these scopes:

openid

profile

w_member_social
