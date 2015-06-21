geany-tags
==========

Geany support for Unity Editor, Leap Motion, CUDA libraries, and more


About
-----

This project provides tag support (keyword autocomplete and parameter hinting) 
for a variety of APIs and platforms in Geany (<http://www.geany.org/>).

In some cases, scripts are provided to generate tag files from a local 
installation for additional customization.


Installation
------------

In the directory for the desired API (see *Supported APIs*), find all .tags 
files and copy them to the Geany tags config directory, usually in the 
following locations:

*   `C:\Users\UserName\Roaming\geany\tags` (Win 7)
*   `C:\Documents and Settings\UserName\Application Data\geany\tags` (Win XP)
*   `~/.config/geany/tags` (*nix)

Autocomplete and hinting features for that API will then be available after a 
restart of Geany.

To use the tags immediately, find *Load Tags* under the *Tools* menu and browse 
to each .tags file in the API directory. More information can be found at 
<http://www.geany.org/manual/current/#tags>.


Supported APIs
--------------

*   Unity 5 (C#): `unity`
*   CUDA (C): `cuda`
*   Android (Java): `android`
