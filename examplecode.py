'''
var isReady = true

function playAudio(chID, guID, adpID, audioFile) {
    isReady = false
    const connection = joinVoiceChannel({
            channelId: chID,
            guildId: guID,
            adapterCreator: adpID,
        })
          
          const player = createAudioPlayer();
          connection.subscribe(player)
          
          const resource = createAudioResource(audioFile)
          player.play(resource)
          player.on(AudioPlayerStatus.Idle, () => {
            connection.destroy()
        });
          
        isReady = true
}
'''