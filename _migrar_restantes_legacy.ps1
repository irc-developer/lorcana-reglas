$ErrorActionPreference='Stop'
$rootRel = "01. Reglas/11. Casos de ejemplo y aclaraciones"
$root = Join-Path (Get-Location) $rootRel
$backupDir = Join-Path $root ("_backup_migracion_restantes_" + (Get-Date -Format 'yyyyMMdd_HHmmss'))
New-Item -ItemType Directory -Path $backupDir | Out-Null

$all = Get-ChildItem -Path $root -File -Filter *.md | Where-Object {
  $_.Name -notin @('Plantilla - Caso de ejemplo y aclaración.md','Glosario.md') -and
  $_.Name -notlike '_backup_migracion*'
}

function Is-Legacy {
  param([string]$text)
  return (
    $text -notmatch '## ❓ Duda' -or
    $text -notmatch '## ✅ Respuesta' -or
    $text -notmatch '## 📘 Fundamento en reglas' -or
    $text -notmatch '## 🔄 Secuencia oficial' -or
    $text -notmatch '## 🏷️ Tags'
  )
}

$targets = @()
foreach($f in $all){
  $raw = Get-Content -LiteralPath $f.FullName -Raw
  if(Is-Legacy $raw){ $targets += $f }
}

function Clean-FrontMatter {
  param([string]$text)
  if($text -match "(?ms)^---\s*\n.*?\n---\s*\n"){
    return ($text -replace "(?ms)^---\s*\n.*?\n---\s*\n","")
  }
  return $text
}

function Get-Section {
  param([string]$text,[string[]]$names)
  foreach($name in $names){
    $pat = "(?ms)^#{1,6}\s*(?:Tema\s*\n)?\s*" + [regex]::Escape($name) + "\s*$\s*(.*?)(?=^#{1,6}\s|\z)"
    $m = [regex]::Match($text,$pat)
    if($m.Success){ return $m.Groups[1].Value.Trim() }
  }
  return ""
}

function Normalize-RuleLink {
  param([string]$link)
  $out = $link
  $out = $out -replace '20\. Reglas CR 1\.X/8\. Zonas \(Zones\)/8\.7\. Bolsa \(Bag\)','7.7. Bolsa (Bag)'
  $out = $out -replace '20\. Reglas CR 1\.X/7\. Habilidades \(abilities\)/7\.4\. Habilidades Disparadas \(Triggered Abilities\)','6.2. Habilidades Disparadas (Triggered Abilities)'
  $out = $out -replace '20\. Reglas CR 1\.X/4\. Estructura del turno \(Turn Structure\)/4\.4\. Final del turno \(End Of Turn Phase\)','3.4. Fase final de turno (End-of-Phase)'
  $out = $out -replace '20\. Reglas CR 1\.X/10\. Palabras clave \(Keywords\)/10\.12\. Cantar Juntos \(Sing Together\)','8.12. Cantar Juntos (Sing Together)'
  $out = $out -replace '20\. Reglas CR 1\.X/',''
  return $out
}

$updated = 0
foreach($f in $targets){
  $raw = Get-Content -LiteralPath $f.FullName -Raw
  Copy-Item -LiteralPath $f.FullName -Destination (Join-Path $backupDir $f.Name)

  $text = Clean-FrontMatter $raw

  $duda = Get-Section $text @('Duda')
  $resp = Get-Section $text @('Respuesta')
  $fund = Get-Section $text @('Fundamento en reglas','Reglas implicadas','Referencias')
  $seq  = Get-Section $text @('Secuencia oficial','Secuencia correcta','Secuencia')

  if([string]::IsNullOrWhiteSpace($duda)){
    $q = [regex]::Match($text,'(?m)^.*\?.*$')
    if($q.Success){ $duda = $q.Value.Trim() }
  }
  if([string]::IsNullOrWhiteSpace($duda)){
    $duda = 'Pendiente de redactar a partir del caso original.'
  }

  if([string]::IsNullOrWhiteSpace($resp)){
    $resp = [regex]::Replace($text,'(?ms)^.*?(?=^#{1,6}\s*(?:📘|Fundamento|Reglas implicadas|Referencias|🔄|Secuencia|🏷️|Tags)\s*$|\z)','').Trim()
  }
  if([string]::IsNullOrWhiteSpace($resp)){
    $resp = 'Pendiente de normalización desde el caso original.'
  }

  $ruleLinks = New-Object System.Collections.Generic.List[string]
  $matches = [regex]::Matches(($fund + "`n" + $text),'\[\[[^\]]+\]\]')
  foreach($m in $matches){
    $lk = $m.Value
    if($lk -match 'Cartas de Lorcana|Set \d|imagenes/|#CR|#Ruling|Discord|WhatsApp'){ continue }
    $norm = Normalize-RuleLink $lk
    if(-not $ruleLinks.Contains($norm)){ $ruleLinks.Add($norm) }
  }
  $ruleLinks = $ruleLinks | Select-Object -First 6
  if($ruleLinks.Count -eq 0){
    $ruleLinks = @(
      '[[6.7. Resolución de Cartas y Efectos (Resolving Cards and Effects)#6.7.2. Resolución|6.7.2. Resolución]]',
      '[[7.7. Bolsa (Bag)#7.7.4. Orden|7.7.4. Orden]]'
    )
  }

  if([string]::IsNullOrWhiteSpace($seq)){
    $seq = @"
1. **Coste**: determinar el coste de la acción o habilidad que inicia la jugada.
2. **Objetivos**: fijar objetivos legales según el texto.
3. **Resolución**: resolver el texto en orden.
4. **Disparos**: añadir a la bolsa los triggers generados y resolver por prioridad.
5. **GSC**: realizar chequeo del estado del juego tras cada resolución.
"@
  }

  $tags = [regex]::Matches($text,'(?m)^#\S+').Value | Select-Object -Unique
  if(-not $tags -or $tags.Count -eq 0){ $tags = @('#Ruling','#Reglas') }

  $fundBlock = ($ruleLinks | ForEach-Object {"- $_"}) -join "`n"
  $tagBlock = ($tags | ForEach-Object {"$_  "}) -join "`n"

  $new = @"
## ❓ Duda

$duda

---

## ✅ Respuesta

$resp

---

## 📘 Fundamento en reglas

$fundBlock

---

## 🔄 Secuencia oficial

$seq

---

## 🏷️ Tags

$tagBlock
"@

  Set-Content -LiteralPath $f.FullName -Value $new -Encoding UTF8
  $updated++
}

Write-Output ("TARGETS=" + $targets.Count)
Write-Output ("UPDATED=" + $updated)
Write-Output ("BACKUP_DIR=" + $backupDir)
