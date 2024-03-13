var myVideo = document.getElementById("videoplaylist");

function playPause() {
    if (myVideo.paused)
        myVideo.play();
    else
        myVideo.pause();
}

function makeBig() {
    myVideo.width = 560;
}

function makeSmall() {
    myVideo.width = 320;
}

function makeNormal() {
    myVideo.width = 420;
}
function restart() {
        var video = document.getElementById("videoplaylist");
        video.currentTime = 0;
    }
function skip(value) {
    var video = document.getElementById("videoplaylist");

    // Add an event listener for the timeupdate event
    video.addEventListener("timeupdate", function onTimeUpdate() {
        // Remove the event listener after the time is updated
        video.removeEventListener("timeupdate", onTimeUpdate);

        var newTime = video.currentTime + value;

        // Ensure the new time is within the valid range (0 to video duration)
        if (newTime < 0) {
            video.currentTime = 0;
        } else if (newTime > video.duration) {
            video.currentTime = video.duration;
        } else {
            video.currentTime = newTime;
        }
    });

    // Check if the video is playing and ready before seeking
    if (video.readyState >= 2 && !video.paused) {
        // Trigger the timeupdate event to execute the logic
        video.dispatchEvent(new Event("timeupdate"));
    }
}


