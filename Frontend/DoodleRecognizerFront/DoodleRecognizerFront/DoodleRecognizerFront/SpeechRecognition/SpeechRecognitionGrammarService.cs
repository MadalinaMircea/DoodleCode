using System;
using System.Collections.Generic;
using System.Linq;
using System.Speech.Recognition;
using System.Text;
using System.Threading.Tasks;

namespace DoodleRecognizerFront
{
    class SpeechRecognitionGrammarService
    {
        public SpeechRecognitionGrammarService()
        {

        }

        public Grammar GetGrammar()
        {
            Choices choices = new Choices();
            choices.Add("pharmacy");
            choices.Add("pharmacist");
            choices.Add("dog");
            choices.Add("butterfly");
            choices.Add("owl");
            choices.Add("computer");
            choices.Add("mother");
            choices.Add("parent");
            GrammarBuilder gb_result = new GrammarBuilder(choices);
            Grammar g_result = new Grammar(gb_result);
            return g_result;
        }
    }
}
