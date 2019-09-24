# ai-aws-deployment

- Used Zappa to deploy - abstraction layer was nice but added debug headache - the app worked locally but not when zappa deployed.

- Poetry was good - solid lessons aquired, will take forward for dep management.

- Discovered a strange error reading pickles as string from S3, reslved with a file download then load on local system... this diff could have changed some zappa assumption.
