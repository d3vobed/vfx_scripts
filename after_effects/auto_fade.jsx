app.beginUndoGroup("Auto Fade In/Out");

var comp = app.project.activeItem;
if (comp instanceof CompItem) {
    var fadeDur = 15; // frames
    for (var i = 0; i < comp.selectedLayers.length; i++) {
        var lyr = comp.selectedLayers[i];
        var inTime = lyr.inPoint;
        var outTime = lyr.outPoint;
        
        // Fade in
        lyr.opacity.setValueAtTime(inTime, 0);
        lyr.opacity.setValueAtTime(inTime + (fadeDur/comp.frameRate), 100);
        
        // Fade out
        lyr.opacity.setValueAtTime(outTime - (fadeDur/comp.frameRate), 100);
        lyr.opacity.setValueAtTime(outTime, 0);
    }
} else {
    alert("Select a composition with layers!");
}

app.endUndoGroup();
