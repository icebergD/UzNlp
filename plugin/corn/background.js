// The onClicked callback function.
function onClickHandler(info, tab) {
    let json_text = JSON.stringify(info);
    alert(JSON.parse(json_text).selectionText)
    alert(json_text)

    // alert("item " + info.menuItemId + " was clicked");
    // alert("info: " + JSON.stringify(info));
    // alert("tab: " + JSON.stringify(tab));
};

chrome.contextMenus.onClicked.addListener(onClickHandler);

// Set up context menu tree at install time.
chrome.runtime.onInstalled.addListener(function() {
  // Create one test item for each context type.
  var context = "selection";
  var title = "Test '" + context + "' menu item";
  var id = chrome.contextMenus.create({"title": title, "contexts":[context], "id": "context" + context});
  console.log("'" + context + "' item:" + id);
  

  
  // Intentionally create an invalid item, to show off error checking in the
  // create callback.
  console.log("About to try creating an invalid item - an error about " +
      "duplicate item child1 should show up");
  chrome.contextMenus.create({"title": "Oops", "id": "child1"}, function() {
    if (chrome.extension.lastError) {
      console.log("Got expected error: " + chrome.extension.lastError.message);
    }
  });
});