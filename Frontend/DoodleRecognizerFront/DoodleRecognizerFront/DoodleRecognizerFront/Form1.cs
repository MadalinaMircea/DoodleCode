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

namespace DoodleRecognizerFront
{
    public partial class Form1 : Form
    {
        bool isDragging = false;
        int currentX = 0;
        int currentY = 0;
        int xUp = 0;
        int xDown = 0;
        int yUp = 0;
        int yDown = 0;
        Rectangle rectCropArea;

        private static readonly HttpClient client = new HttpClient();

        Image image;
        public Form1()
        {
            InitializeComponent();
            ImagePictureBox.SizeMode = PictureBoxSizeMode.StretchImage;

            ImagePictureBox.Controls.Add(CropPictureBox);
            CropPictureBox.Location = new Point(0, 0);
            CropPictureBox.BackColor = Color.Transparent;
        }

        //async Task PostRequestAsync()
        //{
        //byte[] bytes = ImageToByteArray(ImagePictureBox.Image);
        //string bytesString = Encoding.UTF8.GetString(bytes, 0, bytes.Length);
        //    var values = new Dictionary<string, string>
        //    {
        //        { "doodle", bytesString },
        //        { "pars_funcs", ParamBox.Text },
        //        { "output_file", FileBox.Text }
        //    };

        //    var content = new FormUrlEncodedContent(values);

        //    var response = await client.PostAsync("http://localhost:5000/generate_code", content);

        //    ResponseLabel.Text = await response.Content.ReadAsStringAsync();
        //}

        void PostRequest()
        {
            //var httpWebRequest = (HttpWebRequest)WebRequest.Create("http://localhost:5000/generate_code");
            //httpWebRequest.ContentType = "application/json";
            //httpWebRequest.Method = "POST";

            //byte[] bytes = ImageToByteArray(ImagePictureBox.Image);
            //string bytesString = Encoding.UTF8.GetString(bytes, 0, bytes.Length);

            //string json = "{\"doodle\":\"" + bytesString + "\"," +
            //                  "\"pars_funcs\":\"" + ParamBox.Text + "\"," +
            //                  "\"output_file\":\"" + FileBox.Text + "\"}";

            //RequestLabel.Text = json;
            //RequestLabel.Invalidate();

            //using (var streamWriter = new StreamWriter(httpWebRequest.GetRequestStream()))
            //{
            //    streamWriter.Write(json);
            //}

            //var httpResponse = (HttpWebResponse)httpWebRequest.GetResponse();
            //using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
            //{
            //    ResponseLabel.Text = streamReader.ReadToEnd();
            //}

            byte[] bytes = ImageToByteArray(ImagePictureBox.Image);
            string bytesString = Convert.ToBase64String(bytes);

            var client = new RestClient("http://localhost:5000/generate_code");
            client.Timeout = -1;
            var request = new RestRequest(Method.POST);
            request.AddHeader("Content-Type", "application/json");
            string json = "{\"doodle\":\"" +
                bytesString + "\", \"pars_funcs\": \"" +
                ParamBox.Text + "\", \"output_file\":\"" +
                FileBox.Text + "\"}";
            request.AddParameter("application/json", 
                json, ParameterType.RequestBody);
            IRestResponse response = client.Execute(request);
            ResponseLabel.Text = response.Content;
        }

        public byte[] ImageToByteArray(System.Drawing.Image imageIn)
        {
            using (var ms = new MemoryStream())
            {
                imageIn.Save(ms, imageIn.RawFormat);
                return ms.ToArray();
            }
        }
        void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            xUp = e.X;
            yUp = e.Y;

            Rectangle rec = new Rectangle(xDown, yDown, Math.Abs(xUp - xDown), Math.Abs(yUp - yDown));

            using (Pen pen = new Pen(Color.YellowGreen, 3))
            {

                ImagePictureBox.CreateGraphics().DrawRectangle(pen, rec);
            }

            xDown = xDown * ImagePictureBox.Image.Width / ImagePictureBox.Width;
            yDown = yDown * ImagePictureBox.Image.Height / ImagePictureBox.Height;

            xUp = xUp * ImagePictureBox.Image.Width / ImagePictureBox.Width;
            yUp = yUp * ImagePictureBox.Image.Height / ImagePictureBox.Height;

            rectCropArea = new Rectangle(xDown, yDown, Math.Abs(xUp - xDown), Math.Abs(yUp - yDown));
        }
        void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            ImagePictureBox.Invalidate();

            xDown = e.X;
            yDown = e.Y;
        }



        #region move picture at runtime
        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
            isDragging = true;

            currentX = e.X;
            currentY = e.Y;
        }

        private void pictureBox2_MouseMove(object sender, MouseEventArgs e)
        {
            if (isDragging)
            {
                CropPictureBox.Top = CropPictureBox.Top + (e.Y - currentY);
                CropPictureBox.Left = CropPictureBox.Left + (e.X - currentX);
            }
        }

        private void pictureBox2_MouseUp(object sender, MouseEventArgs e)
        {
            isDragging = false;
        }
        #endregion

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
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
                image = ImagePictureBox.Image;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Image img = ImagePictureBox.Image;
            img.RotateFlip(RotateFlipType.Rotate90FlipNone);
            ImagePictureBox.Image = img;
        }
        private void button4_Click(object sender, EventArgs e)
        {
            Size size = CropPictureBox.Size;
            size.Width += 10;
            size.Height += 10;
            if (size.Width <= 250 && size.Height <= 250)
            {
                CropPictureBox.Size = size;
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            Size size = CropPictureBox.Size;
            size.Width -= 10;
            size.Height -= 10;
            if (size.Width >= 20 && size.Height >= 20)
            {
                CropPictureBox.Size = size;
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Rectangle recorte = new Rectangle(CropPictureBox.Location.X, CropPictureBox.Location.Y, CropPictureBox.Width, CropPictureBox.Height);

            Image foto = Crop(ImagePictureBox.Image, recorte);
            ImagePictureBox.Image = foto;

            //Rectangle recorte = pictureBox1.RectangleToClient(pictureBox2.RectangleToScreen(pictureBox2.ClientRectangle));
            //Image foto = Crop(pictureBox1.Image, recorte);
            //pictureBox1.Image = foto;

            //try
            //{
            //    pictureBox1.Refresh();
            //    //Prepare a new Bitmap on which the cropped image will be drawn
            //    Bitmap sourceBitmap = new Bitmap(pictureBox1.Image, pictureBox1.Width, pictureBox1.Height);
            //    Graphics g = pictureBox1.CreateGraphics();

            //    //Draw the image on the Graphics object with the new dimesions
            //    g.DrawImage(sourceBitmap, new Rectangle(0, 0, pictureBox1.Width, pictureBox1.Height), rectCropArea, GraphicsUnit.Pixel);
            //    sourceBitmap.Dispose();
            //}
            //catch (Exception ex)
            //{

            //}
        }

        private Image Crop(Image img, Rectangle rect)
        {
            try
            {
                Bitmap bitmap = new Bitmap(img);
                Bitmap croppedBitmap = bitmap.Clone(rect, bitmap.PixelFormat);

                return (Image)(croppedBitmap);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error");

                return null;
            }
        }

        private void GenerateButton_Click(object sender, EventArgs e)
        {
            PostRequest();
        }
    }
}
