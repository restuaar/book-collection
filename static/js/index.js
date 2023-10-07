async function getItems() {
  return fetch("/get-items").then((res) => res.json());
}

async function refreshItems() {
  const items = await getItems();
  let stringAdd = "";

  items.forEach((item) => {
    stringAdd += `<article class="col buku"><div class="card text-white bg-dark shadow-sm"><div class="card-body"><button value="${item.pk}" onclick="deleteItem(${item.pk})" type="submit" class="btn-close btn-close-white position-absolute top-0 end-0 me-2 mt-2"></button><h5 class="card-title fw-bold">${item.fields.name}</h5><p class="card-text">${item.fields.description}</p><div class="d-flex justify-content-between align-items-center"><div class="btn-group"><button onclick="addStock(${item.pk})" type="button" class="btn btn-sm btn-outline-light">+</button><button onclick="subStock(${item.pk})" type="button" class="btn btn-sm btn-outline-light">-</button></div><small class="text-white">${item.fields.amount}</small></div></div></div></article>`;
  });
  
  $(".bookshelf").html(stringAdd);
}

function addItem() {
  fetch("/create-ajax/", {
    method: "POST",
    body: new FormData(document.querySelector("#form-add-buku")),
  }).then((data) => {
    data.text()
    .then((text) => {
      $(".notif-buku-baru").text(text);
      $(".container-notif-buku-baru").show();
      setTimeout(() => {
        $(".container-notif-buku-baru").hide();
      },3000)
    });
    refreshItems();
  }).catch(err => {
    console.log(err);
    alert("Gagal menambah item.");
  });

  document.querySelector("#form-add-buku").reset();
  return false;
}

function deleteItem(id) {
  fetch(`/delete-ajax/`, {
    method: "DELETE",
    body: JSON.stringify({
      id: id
    }),
    headers: {
      'Content-type': 'application/json; charset=UTF-8',
    },
  }).then(res => {
    refreshItems();
    $(".container-notif-buku-baru").hide();
  }).catch(err => {
    console.log(err);
    alert("Gagal menghapus item.");
  })

  // --versi jQuery--
  // $.ajax({
  //   type: "DELETE",
  //   url: `/delete-ajax/${id}/`,
  //   success: function(response) {
  //   },
  //   error: function(error) {
  //     console.log(error);
  //     alert("Gagal menghapus item.");
  //   }
  // })
}

function addStock(id) {
  fetch(`/add-stock/`, {
    method: "PATCH",
    body: JSON.stringify({
      id: id
    }),
    headers: {
      'Content-type': 'application/json; charset=UTF-8',
    },
  }).then(res => {
    refreshItems();
  }).catch(err => {
    console.log(err);
    alert("Gagal menambah stock item.");
  })
}

function subStock(id) {
  fetch(`/sub-stock/`, {
    method: "PATCH",
    body: JSON.stringify({
      id: id
    }),
    headers: {
      'Content-type': 'application/json; charset=UTF-8',
    },
  }).then(res => {
    refreshItems();
  }).catch(err => {
    console.log(err);
    alert("Gagal mengurangi stock item.");
  })
}


if (window.location.href.indexOf("main") != -1) {
  $(".container-notif-buku-baru").hide();
  refreshItems();
}

$("#button_add").click(addItem);
