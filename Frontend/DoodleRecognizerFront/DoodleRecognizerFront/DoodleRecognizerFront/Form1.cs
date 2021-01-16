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

        SpeechToText speechToText = new SpeechToText();

        bool isRecording = false;

        public Form1()
        {
            InitializeComponent();
            ImagePictureBox.SizeMode = PictureBoxSizeMode.StretchImage;

            FirstPanel.Visible = true;
            MainPanel.Visible = false;
            DetectedPanel.Visible = false;
            SpeechPanel.Visible = false;

            Speak("How would you like to proceed?");

            var speechRecogn = speechToText.InitRecording();
            speechRecogn.SpeechRecognized += sre_SpeechRecognized;
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
            
            Speak("Please wait");

            List<string> detected = new List<string>();

            foreach (string det in DetectedBoxList.CheckedItems)
            {
                detected.Add(det);
            }

            GenerateCode(detected);
        }

        void sre_SpeechRecognized(object sender, SpeechRecognizedEventArgs e)
        {
            string txt = e.Result.Text;
            float conf = e.Result.Confidence;
            if (conf < 0.65) return;
            this.Invoke(new MethodInvoker(() =>
            {
                SpokenListBox.Items.Add(txt);
            }));
        }

        private void SpeechChoiceButton_Click(object sender, EventArgs e)
        {
            Clicked();

            SpeechPanel.Visible = true;
            FirstPanel.Visible = false;

            Speak("Press the button to record");
        }

        private void ImagesChoiceButton_Click(object sender, EventArgs e)
        {
            Clicked();

            MainPanel.Visible = true;
            FirstPanel.Visible = false;

            Speak("Choose your picture");
        }

        private void RecordingButton_Click(object sender, EventArgs e)
        {
            isRecording = !isRecording;

            if (isRecording == true)
            {
                RecordingButton.Text = "Stop Recording";
                speechToText.StartRecording();
            }
            else 
            {
                RecordingButton.Text = "Start Recording";
                speechToText.StopRecording();
            }
        }

        void GenerateCode(List<string> detected)
        {

            string output = server.PostRequestGeneration(detected);
            Speak(output);
            MessageBox.Show(output);
        }

        private void SpeechGenerateButton_Click(object sender, EventArgs e)
        {
            Clicked();

            Speak("Please wait");

            List<string> detected = new List<string>();

            foreach (string det in SpokenListBox.Items)
            {
                detected.Add(det);
            }

            GenerateCode(detected);
        }
    }
}