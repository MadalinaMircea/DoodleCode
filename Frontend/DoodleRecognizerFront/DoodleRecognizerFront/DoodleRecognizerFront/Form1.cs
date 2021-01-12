using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net.Http;
using System.IO;
using System.Net;
using RestSharp;
using System.Speech.Synthesis;
using Newtonsoft.Json;
using DoodleRecognizerFront.ServerCommunication;
using System.Speech.Recognition;
using System.Globalization;

namespace DoodleRecognizerFront
{
    public partial class Form1 : Form
    {
        TextToSpeech speech = new TextToSpeech();

        ServerCommunicator server = new ServerCommunicator();

        List<DetectedObject> detected;

        static CultureInfo ci = new CultureInfo("en-us");
        static SpeechRecognitionEngine sre =
          new SpeechRecognitionEngine(ci);

        public Form1()
        {
            InitializeComponent();
            ImagePictureBox.SizeMode = PictureBoxSizeMode.StretchImage;


            MainPanel.Visible = true;
            DetectedPanel.Visible = false;

            Speak("Choose your picture");

            sre.SetInputToDefaultAudioDevice();
            sre.SpeechRecognized += sre_SpeechRecognized;
            Grammar g_HelloGoodbye = GetHelloGoodbyeGrammar();
            Grammar g_SetTextBox = GetTextBox1TextGrammar();
            sre.LoadGrammarAsync(g_HelloGoodbye);
            sre.LoadGrammarAsync(g_SetTextBox);
            // sre.RecognizeAsync() is in CheckBox event
        }

        static Grammar GetHelloGoodbyeGrammar()
        {
            Choices ch_HelloGoodbye = new Choices();
            ch_HelloGoodbye.Add("hello");
            ch_HelloGoodbye.Add("goodbye");
            GrammarBuilder gb_result =
              new GrammarBuilder(ch_HelloGoodbye);
            Grammar g_result = new Grammar(gb_result);
            return g_result;
        }
        static Grammar GetTextBox1TextGrammar()
        {
            Choices ch_Colors = new Choices();
            ch_Colors.Add(new string[] { "red", "white", "blue" });
            GrammarBuilder gb_result = new GrammarBuilder();
            gb_result.Append("set text box 1");
            gb_result.Append(ch_Colors);
            Grammar g_result = new Grammar(gb_result);
            return g_result;
        }

        public byte[] ImageToByteArray(System.Drawing.Image imageIn)
        {
            using (var ms = new MemoryStream())
            {
                imageIn.Save(ms, imageIn.RawFormat);
                return ms.ToArray();
            }
        }
        private void button1_Click(object sender, EventArgs e)
        {
            Clicked();

            openFileDialog1 = new OpenFileDialog
            {
                InitialDirectory = @"D:\",
                Title = "Select the image",

                CheckFileExists = true,
                CheckPathExists = true,

                DefaultExt = "jpg",
                Filter = "Image files(*.jpg, *.jpeg, *.jpe, *.jfif, *.png) | *.jpg; *.jpeg; *.jpe; *.jfif; *.png",
                FilterIndex = 2,
                RestoreDirectory = true,

                ReadOnlyChecked = true,
                ShowReadOnly = true
            };

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                ImagePictureBox.Load(openFileDialog1.FileName);
                //image = ImagePictureBox.Image;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Image img = ImagePictureBox.Image;
            img.RotateFlip(RotateFlipType.Rotate90FlipNone);
            ImagePictureBox.Image = img;
        }

        private void DetectedBoxList_SelectedIndexChanged(object sender, EventArgs e)
        {
            string text = (string)DetectedBoxList.SelectedItem;

            string check = DetectedBoxList.CheckedItems.Contains(DetectedBoxList.SelectedItem) ?
                ", selected" : ", not selected";

            Speak(text + check);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Clicked();
            Speak("Please wait");

            try
            {
                byte[] bytes = ImageToByteArray(ImagePictureBox.Image);

                List<string> detected;

                string error = server.PostRequestDetection(bytes, out detected);

                if (error.Trim() == "")
                {
                    foreach (string det in detected)
                    {
                        DetectedBoxList.Items.Add(det, true);
                    }

                    DetectedPanel.Visible = true;
                    MainPanel.Visible = false;

                    Speak("Choose your objects of interest");
                    
                }
                else
                {
                    MessageBox.Show("1" + error + "2");
                }
            }
            catch(Exception ex)
            {
                Speak("There was an error. Sorry!");
                MessageBox.Show("There was an error. Sorry! " + ex.Message);
            }
        }

        void Speak(string text)
        {
            speech.Speak(text);
        }

        private void Button_MouseEnter(object sender, EventArgs e)
        {
            Speak((sender as Button).Text);
        }
        void Clicked()
        {
            Speak("Clicked");
        }

        private void GenerateCodeButton_Click(object sender, EventArgs e)
        {
            Clicked();

            List<string> detected = new List<string>();

            foreach (string det in DetectedBoxList.CheckedItems)
            {
                detected.Add(det);
            }

            MessageBox.Show(server.PostRequestGeneration(detected));
        }

        void sr_SpeechRecognized(object sender, SpeechRecognizedEventArgs e)
        {
            MessageBox.Show("hello user");
        }
        private void checkBox1_CheckedChanged(object sender,
      EventArgs e)
        {
            if (checkBox1.Checked == true)
            {
                richTextBox1.Text = "recording";
                sre.RecognizeAsync(RecognizeMode.Multiple);
            }
            else if (checkBox1.Checked == false) // Turn off
            {
                richTextBox1.Text = "not recording";
                sre.RecognizeAsyncCancel();
            }
        }
        void sre_SpeechRecognized(object sender,
          SpeechRecognizedEventArgs e)
        {
            richTextBox1.Text = "recognizing";
            string txt = e.Result.Text;
            float conf = e.Result.Confidence;
            if (conf < 0.65) return;
            this.Invoke(new MethodInvoker(() =>
            {
                listBox1.Items.Add("I heard you say: "
              + txt);
            })); // WinForm specific
            //if (txt.IndexOf("text") >= 0 && txt.IndexOf("box") >=
            //  0 && txt.IndexOf("1") >= 0)
            //{
            //    string[] words = txt.Split(' ');
            //    this.Invoke(new MethodInvoker(() =>
            //    { textBox1.Text = words[4]; })); // WinForm specific
            //}
        }
    }
}