<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="1.1">
    <xsl:output method="text"/>
    <xsl:variable name='nl'><xsl:text>&#xa;</xsl:text></xsl:variable>
    <xsl:template match="/" >
        <xsl:text>id;name;type;v1;v2;v3</xsl:text><xsl:value-of select="$nl"/>
        <xsl:apply-templates select="/structure/automaton/state"/>
        <xsl:apply-templates select="/structure/automaton/transition"/>
    </xsl:template>
    <xsl:template match="state">
        <xsl:variable name="id" select="@id"/>
        <xsl:variable name="name" select="@name"/>
        <xsl:variable name='initial' select="./initial"/>
        <xsl:variable name='final' select="./final"/>
        <xsl:value-of select="concat($id,';',$name,';state;',$initial,';',$final,';',$nl)"/>
    </xsl:template>
    <xsl:template match="transition">
        <xsl:variable name="source" select="./from/text()"/>
        <xsl:variable name="cible" select="./to/text()"/>
        <xsl:variable name="symbol" select="./read/text()"/>
        <xsl:variable name="id"><xsl:number level="single" format="1"/></xsl:variable>
        <xsl:variable name="name" select="concat($source,$symbol,$cible)"/>
        <xsl:value-of select="concat($id,';',$name,';transition;',$source,';',$symbol,';',$cible,$nl)"/>
    </xsl:template>
</xsl:stylesheet>