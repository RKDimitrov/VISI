import win32com.client

def check_windows_update():
    # Connect to the Windows Update API
    update_session = win32com.client.Dispatch('Microsoft.Update.Session')

    # Get a list of available updates
    update_searcher = update_session.CreateUpdateSearcher()
    search_result = update_searcher.Search('IsInstalled=0')

    # Check if there are any available updates
    if search_result.Updates.Count == 0:
        return ('Your Windows operating system is up to date.', True)
    else:
        updates = [update.Title for update in search_result.Updates]
        update_list = '\n- '.join(updates)
        return f'There are {search_result.Updates.Count} available Windows updates:\n- {update_list}'

