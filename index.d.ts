// Type definitions for pcutil
// Project: pcutil

export function askForCalendarAccess(): Promise<'authorized' | 'denied'>
export function askForContactsAccess(): Promise<'authorized' | 'denied'>
export function askForFoldersAccess(): Promise<'authorized' | 'denied'>
export function askForFullDiskAccess(): undefined
export function askForRemindersAccess(): Promise<'authorized' | 'denied'>
export function askForCameraAccess(): Promise<'authorized' | 'denied' | 'restricted'>
export function askForMicrophoneAccess(): Promise<'authorized' | 'denied' | 'restricted'>
export function askForPhotosAccess(): Promise<'authorized' | 'denied' | 'restricted'>
export function askForSpeechRecognitionAccess(): Promise<'authorized' | 'denied'>
export function askForScreenCaptureAccess(): undefined
export function askForAccessibilityAccess(): undefined
export function getAuthStatus(authType: AuthType): PermissionType
export function enumerateWindows(): Array<Window>
export function enumerateDisplay(): Array<String>
export type AuthType =
  | 'contacts'
  | 'calendar'
  | 'reminders'
  | 'full-disk-access'
  | 'camera'
  | 'photos'
  | 'speech-recognition'
  | 'microphone'
  | 'accessibility'
  | 'location'
  | 'screen'

export type PermissionType = 'not determined' | 'denied' | 'authorized' | 'restricted'

export interface Window {
  title: String
  id: String
}
