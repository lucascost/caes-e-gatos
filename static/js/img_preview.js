const inputFile = document.querySelector("#id_image");
const imgPreview = document.getElementById("img_preview");
const imgTxt = "Escolha uma imagem";
imgPreview.innerHTML = imgTxt;

function loadImg(src) {
  const img = document.createElement("img");
  img.src = src;
  img.classList.add("picture-label");

  imgPreview.innerHTML = "";
  imgPreview.appendChild(img);

  document.querySelector(".add-img-icon").style.display = "none";
}

inputFile.addEventListener("change", function (e) {
  const inputTarget = e.target;
  const file = inputTarget.files[0];

  if (file) {
    const reader = new FileReader();

    reader.addEventListener("load", function (e) {
      const readerTarget = e.target;

      const img = document.createElement("img");
      img.src = readerTarget.result;
      img.classList.add("picture-label");

      imgPreview.innerHTML = "";
      imgPreview.appendChild(img);

    });

    reader.readAsDataURL(file);
  } else {
    imgPreview.innerHTML = imgTxt;
    document.querySelector(".add-img-icon").style.display = "block";
  }
});

inputFile.addEventListener("click", () => loadImg(''));
