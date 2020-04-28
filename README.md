[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
 [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![Actions Status](https://github.com/codebytere/node-mac-permissions/workflows/Test/badge.svg)](https://github.com/codebytere/node-mac-permissions/actions)

# node-mac-permissions

```js
$ npm i node-mac-permissions
```

This native Node.js module allows you to manage an app's access to:

* Contacts
* Full Disk Access
* Calendar
* Reminders
* Camera
* Microphone
* Accessibility
* Location
* Screen Capture

## API

## `permissions.getAuthStatus(type)`

* `type` String - The type of system component to which you are requesting access. Can be one of `accessibility`, `calendar`, `camera`, `contacts`, `full-disk-access`, `location`, `microphone`, `screen`, or `reminders`.

Returns `String` - Can be one of `not determined`, `denied`, `authorized`, or `restricted`.

Checks the authorization status of the application to access `type` on macOS.

Return Value Descriptions: 
* `not determined` - The user has not yet made a choice regarding whether the application may access `type` data.
* `restricted` - The application is not authorized to access `type` data. The user cannot change this application’s status, possibly due to active restrictions such as parental controls being in place.
* `denied` - The user explicitly denied access to `type` data for the application.
* `authorized` - The application is authorized to access `type` data.

**Notes:**
  * Access to `contacts` will always return a status of `authorized` prior to macOS 10.11, as access to contacts was unilaterally allowed until that version.
  * Access to `camera` and `microphone` will always return a status of `authorized` prior to macOS 10.14, as access to contacts was unilaterally allowed until that version.
  * Access to `screen` will always return a status of `authorized` prior to macOS 10.15, as access to screen capture was unilaterally allowed until that version.

Example:
```js
const types = [
  'contacts',
  'calendar',
  'reminders',
  'full-disk-access',
  'camera',
  'microphone',
  'accessibility',
  'location'
]

const statuses = ['not determined', 'denied', 'authorized', 'restricted']
for (const type of types) {
  const status = getAuthStatus(type)
  console.log(`Access to ${type} is ${status}`)
}
```

## `permissions.askForContactsAccess()`

Returns `Promise<String>` - Whether or not the request succeeded or failed; can be `authorized` or `denied`.

Your app’s `Info.plist` file must provide a value for the `NSContactsUsageDescription` key that explains to the user why your app is requesting Contacts access.

```
<key>NSContactsUsageDescription</key>
<string>Your reason for wanting to access the Contact store</string>
```

**Note:** `status` will be resolved back as `authorized` prior to macOS 10.11, as access to contacts was unilaterally allowed until that version.

Example:
```js
const { askForContactsAccess } = require('node-mac-permissions')

askForContactsAccess().then(status => {
  console.log(`Access to Contacts is ${status}`)
})
```

## `permissions.askForCalendarAccess()`

Returns `Promise<String>` - Whether or not the request succeeded or failed; can be `authorized` or `denied`.

Example:
```js
const { askForCalendarAccess } = require('node-mac-permissions')

askForCalendarAccess().then(status => {
  console.log(`Access to Calendar is ${status}`)
})
```

## `permissions.askForRemindersAccess()`

Returns `Promise<String>` - Whether or not the request succeeded or failed; can be `authorized` or `denied`.

Example:
```js
const { askForRemindersAccess } = require('node-mac-permissions')

askForRemindersAccess().then(status => {
  console.log(`Access to Reminders is ${status}`)
})
```

## `permissions.askForFullDiskAccess()`

There is no API for programmatically requesting Full Disk Access on macOS at this time, and so calling this method will trigger opening of System Preferences at the Full Disk pane of Security and Privacy.

Example:

```js
const { askForFullDiskAccess } = require('node-mac-permissions')

askForFullDiskAccess()
```

## `permissions.askForCameraAccess()`

Returns `Promise<String>` - Current permission status; can be `authorized`, `denied`, or `restricted`.

Checks the authorization status for camera access. If the status check returns:

* `not determined` - The camera access authorization will prompt the user to authorize or deny. The Promise is resolved after the user selection with either `authorized` or `denied`.
* `denied` - The `Security & Privacy` System Preferences window is opened with the Camera privacy key highlighted. On open of the `Security & Privacy` window, the Promise is resolved as `denied`.
* `restricted` - The Promise is resolved as `restricted`.

Your app must provide an explanation for its use of capture devices using the `NSCameraUsageDescription` `Info.plist` key; Calling this method or attempting to start a capture session without a usage description raises an exception.

```
<key>NSCameraUsageDescription</key>
<string>Your reason for wanting to access the Camera</string>
```

**Note:**

- `status` will be resolved back as `authorized` prior to macOS 10.14 High Sierra, as access to the camera and microphone was unilaterally allowed until that version.

Example:

```js
const { askForCameraAccess } = require("node-mac-permissions");

const status = await askForCameraAccess();
```

## `permissions.askForMicrophoneAccess()`

Returns `Promise<String>` - Current permission status; can be `authorized`, `denied`, or `restricted`.

Checks the authorization status for microphone access. If the status check returns:

* `not determined` - The microphone access authorization will prompt the user to authorize or deny. The Promise is resolved after the user selection with either `authorized` or `denied`.
* `denied` -T he `Security & Privacy` System Preferences window is opened with the Microphone privacy key highlighted. On open of the `Security & Privacy` window, the Promise is resolved as `denied`.
* `restricted` - The Promise is resolved as `restricted`.

Your app must provide an explanation for its use of capture devices using the `NSMicrophoneUsageDescription` `Info.plist` key; Calling this method or attempting to start a capture session without a usage description raises an exception.

```
<key>NSMicrophoneUsageDescription</key>
<string>Your reason for wanting to access the Microphone</string>
```

**Note:**

- `status` will be resolved back as `authorized` prior to macOS 10.14 High Sierra, as access to the camera and microphone was unilaterally allowed until that version.

Example:

```js
const { askForMicrophoneAccess } = require("node-mac-permissions");

const status = await askForMicrophoneAccess();
```

## `permissions.askForScreenCaptureAccess()`

There is no API for programmatically requesting Screen Capture on macOS at this time, and so calling this method will trigger opening of System Preferences at the Screen Capture pane of Security and Privacy.

Example:

```js
const { askForScreenCaptureAccess } = require('node-mac-permissions')

askForScreenCaptureAccess()
```

## `permissions.askForAccessibilityAccess()`

There is no API for programmatically requesting Accessibility access on macOS at this time, and so calling this method will trigger opening of System Preferences at the Accessibility pane of Security and Privacy.

Example:

```js
const { askForAccessibilityAccess } = require('node-mac-permissions')

askForAccessibilityAccess()
```

## FAQ

Q. I'm seeing an error like the following when using webpack:

```sh
App threw an error during load
TypeError: Cannot read property 'indexOf' of undefined
    at Function.getFileName (webpack-internal:///./node_modules/bindings/bindings.js:178:16)
```

A. This error means that webpack packed this module, which it should not. To fix this, you should configure webpack to use this module externally, e.g explicitly not pack it.

----------------------

Q. I've authorized access to a particular system component and want to reset it. How do I do that?

A. You can use `tccutil` to do this!

The `tccutil` command manages the privacy database, which stores decisions the user has made about whether apps may access personal data.

Examples:

```sh
# Reset all app permissions
$ tccutil reset All

# Reset Accessibility access permissions
$ tccutil reset Accessibility

# Reset Reminders access permissions
$ tccutil reset Reminders

# Reset Calendar access permissions
$ tccutil reset Calendar

# Reset Camera access permissions
$ tccutil reset Camera

# Reset Microphone access permissions
$ tccutil reset Microphone
```
