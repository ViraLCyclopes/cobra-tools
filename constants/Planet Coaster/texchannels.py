texchannels = {
	'pAOSamplerTexture': {"": "AO"},
	'pBaseColourTexture': {"RGB": "BC", "A": ""},  # unsure about A
	# 'pCavitySmoothnessArrayTexture': {"": ""},
	# 'pCavitySmoothnessOpacitySamplerTexture': {"R": "", "G": "", "B": "", "A": ""},
	'pCavitySmoothnessSamplerTexture': {"R": "CA", "G": "SM", "B": "", "A": "FO"},  # B, A unused in dino mascot, but needed in hol_baubles_01 for flexi
	# 'pCoarseNoiseTexture': {"": ""},
	# 'pDiffuseArrayTexture': {"": ""},
	'pDiffuseOpacityTexture': {"RGB": "BC", "A": "OP"},
	'pDiffuseTexture': {"": "BC"},
	'pEmissiveOpacityTexture': {"RGB": "EM", "A": "OP"},
	'pEmissiveTexture': {"": "EM"},
	'pFlexiColourMasksSamplerTexture': {"R": "F1", "G": "F2", "B": "F3", "A": "F4"},
	# 'pFoamMapTexture': {"": ""},
	# 'pGradHeightArrayTexture': {"RG": "", "B": "", "A": ""},
	# 'pLightSequenceTexture': {"": ""},
	# 'pMacroDiffuseTexture': {"": ""},
	'pMetalSmoothnessCavityOpacitySamplerTexture': {"R": "MT", "G": "SM", "B": "CA", "A": "OP"},
	'pMetalSmoothnessCavitySamplerTexture': {"R": "MT", "G": "SM", "B": "CA", "A": ""},
	# 'pMist0Texture': {"": ""},
	# 'pMist1Texture': {"": ""},
	'pNormalTexture': {"RG": "NM"},
	'pOpacityMapTexture': {"": "OP"},
	# 'pRibbonMask1Texture': {"": ""},
	# 'pShoreWavesTexture': {"": ""},
	# 'pSkirtDiffuseArrayTexture': {"": ""},
	# 'pSkirtMaterialMaskTexture': {"": ""},
	# 'pSkirtNormalsTexture': {"": ""},
	# 'pSpecularArrayTexture': {"": ""},
	'pSpecularSamplerTexture': {"": "SP"},
	# 'pSpecularSmoothnessSamplerTexture': {"R": "", "G": "", "B": "", "A": ""},
	# 'pWaterDetailNormalMapTexture': {"": ""},
	# 'pWaterFoamMapTexture': {"": ""},
	# 'pWaterHighFreqDetailNormalMapTexture': {"": ""},
	'pSpecularSmoothnessSamplerTexture': {"": "SP"}, # path materials
	'pCavitySmoothnessAOSamplerTexture': {"R": "CA", "G": "SM", "B": "AO", "A": ""},  # path materials

}
