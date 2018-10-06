function speakText(text, wait_time) {
    var dfd = jQuery.Deferred();
    speechSynthesis.onvoiceschanged = function () {
        voices = speechSynthesis.getVoices();
        var msg = new SpeechSynthesisUtterance(text);
        var voices = window.speechSynthesis.getVoices();
        msg.lang = 'ru-RU';

        msg.voice = voices[window.default_voice_id];
        speechSynthesis.speak(msg);
        window.setTimeout(function () {
            dfd.resolve(true);
        }, wait_time);
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
    console.log(textToButton);

    var recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.lang = 'ru-RU';
    recognition.start();

    recognition.onresult = function (event) {
        var interim_transcript = '';
        for (var i = event.resultIndex; i < event.results.length; ++i) {
            interim_transcript += event.results[i][0].transcript;
            console.log(interim_transcript);
        }

        var interim_transcript_lower = interim_transcript.toLowerCase()
        for (var i = 0; i < textToButton.length; i++) {
            if (interim_transcript_lower.indexOf(textToButton[i].matchString)) {
                textToButton[i].button.click()
            }
        }
    }
}