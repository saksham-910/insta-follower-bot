```markdown
# Instagram Follower Bot 📸

A Selenium bot that logs into an Instagram clone, searches for 
a target account in a chosen niche, scrolls through their 
followers list, and automatically follows all visible followers.

## What it does
- Logs into the platform automatically
- Searches for and navigates to a target account's profile
- Opens the followers popup and auto-scrolls it to load more 
  followers beyond the initial batch
- Clicks "Follow" on each follower, handling already-followed 
  accounts (which trigger an unfollow confirmation popup) 
  gracefully by dismissing the popup and continuing

## How to run
1. Install dependencies:
```
pip install selenium
```
2. Update the credentials and target account:
```python
similar_account = 'target_username'
username = 'your_email'
passw = 'your_password'
```
3. Run the script:
```
python main.py
```

## Concepts used
- Selenium WebDriver automation
- Scrolling within a popup/modal (separate from the main page)
  using JavaScript (`scrollTop` / `scrollHeight`)
- JavaScript-based clicking to bypass UI overlay interception
- Exception handling for dynamic "already following" popups
- Working with lists of elements via `find_elements`

## Notes
Built against a safe Instagram-clone practice environment 
(share-a-naan) rather than the real Instagram platform, to 
avoid triggering anti-automation measures on a live social 
media service.
```
