const pcutil = require('bindings')('pc-util.node')

function getAuthStatus(type) {
  const validTypes = [
    'contacts',
    'calendar',
    'reminders',
    'full-disk-access',
    'camera',
    'photos',
    'speech-recognition',
    'microphone',
    'accessibility',
    'location',
    'screen',
    'bluetooth',
  ]

  if (!validTypes.includes(type)) {
    throw new TypeError(`${type} is not a valid type`)
  }

  return pcutil.getAuthStatus.call(this, type)
}

function askForFoldersAccess(folder) {
  const validFolders = ['desktop', 'documents', 'downloads']

  if (!validFolders.includes(folder)) {
    throw new TypeError(`${folder} is not a valid protected folder`)
  }

  return pcutil.askForFoldersAccess.call(this, folder)
}

module.exports = {
  askForCalendarAccess: pcutil.askForCalendarAccess,
  askForContactsAccess: pcutil.askForContactsAccess,
  askForFoldersAccess,
  askForFullDiskAccess: pcutil.askForFullDiskAccess,
  askForRemindersAccess: pcutil.askForRemindersAccess,
  askForCameraAccess: pcutil.askForCameraAccess,
  askForMicrophoneAccess: pcutil.askForMicrophoneAccess,
  askForPhotosAccess: pcutil.askForPhotosAccess,
  askForSpeechRecognitionAccess: pcutil.askForSpeechRecognitionAccess,
  askForScreenCaptureAccess: pcutil.askForScreenCaptureAccess,
  askForAccessibilityAccess: pcutil.askForAccessibilityAccess,
  getAuthStatus,
  enumerateWindows: pcutil.enumerateWindows,
  enumerateDisplay: pcutil.enumerateDisplay,
}
