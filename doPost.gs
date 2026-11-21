// Tambahkan di Code.gs (di bawah doGet). Dipakai oleh aplikasi APK.
function doPost(e) {
  var r;
  try {
    var b = JSON.parse(e.postData.contents);
    r = api(b.t, b.op, b.a);
  } catch (x) {
    r = { err: 'Server: ' + x.message };
  }
  return ContentService.createTextOutput(JSON.stringify(r === undefined ? null : r))
    .setMimeType(ContentService.MimeType.JSON);
}
