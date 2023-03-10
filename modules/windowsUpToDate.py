import win32com.client

# Connect to the Windows Update API
update_session = win32com.client.Dispatch('Microsoft.Update.Session')

# Get a list of available updates
update_searcher = update_session.CreateUpdateSearcher()
search_result = update_searcher.Search('IsInstalled=0')

# Check if there are any available updates
if search_result.Updates.Count == 0:
    print('Your Windows operating system is up to date.')
else:
    print(f'There are {search_result.Updates.Count} available updates:')
    for update in search_result.Updates:
        print(f'- {update.Title}')
