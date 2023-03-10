import win32com.client

# Initialize the Windows Update Agent API
wua = win32com.client.Dispatch("Microsoft.Update.Session")

# Search for available updates
searcher = wua.CreateUpdateSearcher()
searcher.Online = True
result = searcher.Search("IsInstalled=0")

if result.Updates.Count > 0:
    print("There are updates available.")
else:
    print("Your system is up to date.")
