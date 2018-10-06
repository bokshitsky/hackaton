function speakText(text, wait_time) {
    var dfd = jQuery.Deferred();
    speechSynthesis.onvoiceschanged = function () {
        voices = speechSynthesis.getVoices();
        var msg = new SpeechSynthesisUtterance(text);
        var voices = window.speechSynthesis.getVoices();
        msg.lang = 'ru-RU';
        msg.pitch = 1;
        msg.voice = voices[window.default_voice_id];
        speechSynthesis.speak(msg);

        var interval;
        interval = setInterval(function () {
            if (speechSynthesis.speaking) {
                return;
            }
            clearInterval(interval);
            dfd.resolve(true);
        });
        speechSynthesis.onvoiceschanged = null
    };
    return dfd.promise()
}

function listenVoice() {
    var voiceButtons = $('.voice_button');

    var textToButton = [];
    voiceButtons.each(function (index, button) {
        var matchingString = button.getAttribute('voice_data');
        var matchers = matchingString.toLowerCase().split('|');
        for (var i = 0; i < matchers.length; i++) {
            textToButton.push({
                matchString: matchers[i],
                button: button
            })
        }
    });
    textToButton.sort(function (a, b) {
        return b.matchString.length - a.matchString.length
    });

    console.log(textToButton);

    var recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.lang = 'ru-RU';
    recognition.start();

    recognition.onresult = function (event) {
        var speachstate = '';
        for (var i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
                speachstate += event.results[i][0].transcript;
            }
        }

        var speachstateLower = speachstate.toLowerCase();
        for (var i = 0; i < textToButton.length; i++) {
            if (speachstateLower.indexOf(textToButton[i].matchString) != -1) {
                textToButton[i].button.click()
            }
        }
    }
}