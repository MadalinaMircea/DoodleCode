using System;
using System.Collections.Generic;
using System.Linq;
using System.Speech.Synthesis;
using System.Text;
using System.Threading.Tasks;

namespace DoodleRecognizerFront
{
    class TextToSpeech
    {
        SpeechSynthesizer synthesizer;

        public TextToSpeech()
        {
            synthesizer = new SpeechSynthesizer();
            synthesizer.SetOutputToDefaultAudioDevice();
        }

        public void Speak(string text)
        {
            synthesizer.SpeakAsyncCancelAll();
            synthesizer.SpeakAsync(text);
        }
    }
}
