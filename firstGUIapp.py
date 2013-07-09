import android
droid = android.Android()
droid.dialogSetPositiveButtonTexe('OK')
droid.dialogShow()
resp = droid.dialogGetResponse().result
droid.makeToast('Later')
