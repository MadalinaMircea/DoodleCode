using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Speech.Recognition;
using System.Text;
using System.Threading.Tasks;

namespace DoodleRecognizerFront
{
    class SpeechToText
    {
        static CultureInfo ci = new CultureInfo("en-us");
        SpeechRecognitionEngine sre =  new SpeechRecognitionEngine(ci);
        SpeechRecognitionGrammarService grammarService = new SpeechRecognitionGrammarService();
        public SpeechToText()
        {
        }

        public SpeechRecognitionEngine InitRecording()
        {
            sre.SetInputToDefaultAudioDevice();
            Grammar speechGrammar = grammarService.GetGrammar();
            sre.LoadGrammarAsync(speechGrammar);

            return sre;
        }


        public void StartRecording()
        {
            sre.RecognizeAsync(RecognizeMode.Multiple);
        }

        public void StopRecording()
        {
            sre.RecognizeAsyncCancel();
        }
    }
}
